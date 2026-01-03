// Code Train - Frontend Application
const API_BASE_URL = window.location.origin + '/api';

// Global state
let currentUser = null;
let codeEditor = null;
let authToken = localStorage.getItem('authToken');

// Initialize app on page load
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});

async function initializeApp() {
    // Check privacy policy acceptance
    checkPrivacyPolicyAcceptance();

    // Check authentication
    await checkAuth();

    // Initialize page-specific functionality
    const currentPage = getCurrentPage();

    // Setup common event listeners
    setupCommonEventListeners();

    // Initialize based on current page
    switch(currentPage) {
        case 'home':
            initHomePage();
            break;
        case 'problems':
            initProblemsPage();
            break;
        case 'problem-detail':
            initProblemDetailPage();
            break;
        case 'leaderboard':
            initLeaderboardPage();
            break;
        case 'profile':
            initProfilePage();
            break;
    }
}

function getCurrentPage() {
    // Determine current page from URL
    const path = window.location.pathname;

    if (path === '/' || path === '') {
        return 'home';
    } else if (path === '/problems/') {
        return 'problems';
    } else if (path.startsWith('/problems/')) {
        return 'problem-detail';
    } else if (path === '/leaderboard/') {
        return 'leaderboard';
    } else if (path === '/profile/') {
        return 'profile';
    }

    return 'unknown';
}

// PRIVACY POLICY MODAL

function checkPrivacyPolicyAcceptance() {
    const privacyAccepted = localStorage.getItem('privacyPolicyAccepted');

    if (!privacyAccepted) {
        // Show privacy modal after a short delay for better UX
        setTimeout(() => {
            showPrivacyModal();
        }, 500);
    }
}

function showPrivacyModal() {
    const privacyModal = document.getElementById('privacyModal');
    const acceptBtn = document.getElementById('acceptPrivacyBtn');

    if (privacyModal) {
        privacyModal.style.display = 'flex';

        // Prevent scrolling when modal is open
        document.body.style.overflow = 'hidden';

        // Handle accept button click
        acceptBtn.addEventListener('click', () => {
            acceptPrivacyPolicy();
        });
    }
}

function acceptPrivacyPolicy() {
    // Store acceptance in localStorage
    localStorage.setItem('privacyPolicyAccepted', 'true');
    localStorage.setItem('privacyPolicyAcceptedDate', new Date().toISOString());

    // Hide modal with animation
    const privacyModal = document.getElementById('privacyModal');
    privacyModal.style.animation = 'fadeOut 0.3s ease-in-out';

    setTimeout(() => {
        privacyModal.style.display = 'none';
        privacyModal.style.animation = '';
        document.body.style.overflow = '';
    }, 300);
}

// Add fadeOut animation to CSS if not exists
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeOut {
        from {
            opacity: 1;
        }
        to {
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ============================================================================
// COMMON EVENT LISTENERS
// ============================================================================

function setupCommonEventListeners() {
    // Mobile Navigation / Hamburger Menu
    const navbarToggle = document.getElementById('navbarToggle');
    const navbarMenu = document.getElementById('navbarMenu');
    const navbarOverlay = document.getElementById('navbarOverlay');

    if (navbarToggle && navbarMenu && navbarOverlay) {
        // Toggle mobile menu
        navbarToggle.addEventListener('click', () => {
            navbarToggle.classList.toggle('active');
            navbarMenu.classList.toggle('active');
            navbarOverlay.classList.toggle('active');

            // Prevent body scroll when menu is open
            if (navbarMenu.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });

        // Close menu when clicking overlay
        navbarOverlay.addEventListener('click', () => {
            navbarToggle.classList.remove('active');
            navbarMenu.classList.remove('active');
            navbarOverlay.classList.remove('active');
            document.body.style.overflow = '';
        });

        // Close menu when clicking any nav link
        const navLinks = navbarMenu.querySelectorAll('.nav-link, .btn');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navbarToggle.classList.remove('active');
                navbarMenu.classList.remove('active');
                navbarOverlay.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Close menu on window resize if getting bigger
        let windowWidth = window.innerWidth;
        window.addEventListener('resize', () => {
            if (window.innerWidth > 968 && window.innerWidth !== windowWidth) {
                navbarToggle.classList.remove('active');
                navbarMenu.classList.remove('active');
                navbarOverlay.classList.remove('active');
                document.body.style.overflow = '';
            }
            windowWidth = window.innerWidth;
        });
    }

    // Auth buttons
    const loginBtn = document.getElementById('loginBtn');
    if (loginBtn) {
        loginBtn.addEventListener('click', () => {
            showModal('login');
        });
    }

    const registerBtn = document.getElementById('registerBtn');
    if (registerBtn) {
        registerBtn.addEventListener('click', () => {
            showModal('register');
        });
    }

    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', logout);
    }

    // Modal
    const closeBtn = document.querySelector('.close');
    if (closeBtn) {
        closeBtn.addEventListener('click', hideModal);
    }

    window.addEventListener('click', (e) => {
        const modal = document.getElementById('authModal');
        if (e.target === modal) {
            hideModal();
        }
    });

    // Modal tabs
    document.querySelectorAll('.modal-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            const tabName = tab.dataset.tab;
            switchAuthTab(tabName);
        });
    });

    // Forms
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }

    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', handleRegister);
        setupRegisterValidation();
    }

    // Privacy Policy link
    const privacyLink = document.getElementById('showPrivacyPolicyLink');
    if (privacyLink) {
        privacyLink.addEventListener('click', (e) => {
            e.preventDefault();
            showPrivacyModal();
        });
    }

    // Privacy Policy link in modal
    const privacyLinkInModal = document.getElementById('privacyLinkInModal');
    if (privacyLinkInModal) {
        privacyLinkInModal.addEventListener('click', (e) => {
            e.preventDefault();
            hideModal(); // Close auth modal first
            setTimeout(() => showPrivacyModal(), 300); // Then show privacy modal
        });
    }
}

function setupRegisterValidation() {
    const usernameInput = document.getElementById('registerUsername');
    const emailInput = document.getElementById('registerEmail');
    const passwordInput = document.getElementById('registerPassword');
    const passwordConfirmInput = document.getElementById('registerPasswordConfirm');

    if (usernameInput) {
        usernameInput.addEventListener('blur', function() {
            if (this.value.trim()) {
                this.classList.remove('invalid');
                this.classList.add('valid');
            } else {
                this.classList.remove('valid');
            }
        });
    }

    if (emailInput) {
        emailInput.addEventListener('blur', function() {
            if (this.value.trim() && this.value.includes('@')) {
                this.classList.remove('invalid');
                this.classList.add('valid');
            } else {
                this.classList.remove('valid');
            }
        });
    }

    if (passwordInput) {
        passwordInput.addEventListener('blur', function() {
            if (this.value.length >= 8) {
                this.classList.remove('invalid');
                this.classList.add('valid');
            } else {
                this.classList.remove('valid');
            }
        });

        passwordInput.addEventListener('input', function() {
            const passwordConfirm = passwordConfirmInput?.value;
            if (passwordConfirm && this.value && this.value === passwordConfirm) {
                passwordConfirmInput.classList.remove('invalid');
                passwordConfirmInput.classList.add('valid');
            } else if (passwordConfirm && this.value !== passwordConfirm) {
                passwordConfirmInput.classList.remove('valid');
            }
        });
    }

    if (passwordConfirmInput) {
        passwordConfirmInput.addEventListener('blur', function() {
            const password = passwordInput?.value;
            if (this.value && password && this.value === password) {
                this.classList.remove('invalid');
                this.classList.add('valid');
            } else {
                this.classList.remove('valid');
            }
        });

        passwordConfirmInput.addEventListener('input', function() {
            const password = passwordInput?.value;
            if (this.value && password && this.value === password) {
                this.classList.remove('invalid');
                this.classList.add('valid');
            } else if (this.value) {
                this.classList.remove('valid');
            }
        });
    }
}

// HOME PAGE

function initHomePage() {
    loadStats();

    // Auto-open login modal if redirected from protected page
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('login') === 'true' && !authToken) {
        showModal('login');
    }

    const getStartedBtn = document.getElementById('getStartedBtn');
    if (getStartedBtn) {
        getStartedBtn.addEventListener('click', () => {
            if (authToken) {
                window.location.href = '/problems/';
            } else {
                showModal();
            }
        });
    }
}

async function loadStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/problems/stats/overall/`);
        const data = await response.json();

        const totalProblems = document.getElementById('totalProblems');
        const totalUsers = document.getElementById('totalUsers');

        if (totalProblems) totalProblems.textContent = data.total_problems || 0;
        if (totalUsers) totalUsers.textContent = data.total_users || 0;
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

// ============================================================================
// PROBLEMS PAGE
// ============================================================================

function initProblemsPage() {
    // Redirect to home if not authenticated
    if (!authToken) {
        window.location.href = '/?login=true';
        return;
    }

    loadProblems();

    const difficultyFilter = document.getElementById('difficultyFilter');
    if (difficultyFilter) {
        difficultyFilter.addEventListener('change', () => loadProblems(1));
    }

    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', debounce(() => loadProblems(1), 500));
    }
}

let currentPage = 1;
let paginationData = null;

async function loadProblems(page = 1) {
    const difficulty = document.getElementById('difficultyFilter')?.value || '';
    const search = document.getElementById('searchInput')?.value || '';

    let url = `${API_BASE_URL}/problems/`;
    const params = new URLSearchParams();

    if (difficulty) params.append('difficulty', difficulty);
    if (search) params.append('search', search);
    params.append('page', page);

    if (params.toString()) {
        url += '?' + params.toString();
    }

    const headers = {};
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`;
    }

    try {
        const response = await fetch(url, { headers });
        const data = await response.json();

        currentPage = page;
        paginationData = {
            count: data.count,
            next: data.next,
            previous: data.previous
        };

        displayProblems(data.results || data);
        displayPagination();

        // Scroll to top of problems list
        const problemsSection = document.querySelector('.problems-section');
        if (problemsSection && page !== 1) {
            problemsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    } catch (error) {
        console.error('Error loading problems:', error);
        const problemsList = document.getElementById('problemsList');
        if (problemsList) {
            problemsList.innerHTML = '<p class="error">Błąd wczytywania zadań. Spróbuj ponownie później.</p>';
        }
    }
}

function displayProblems(problems) {
    const problemsList = document.getElementById('problemsList');
    if (!problemsList) return;

    if (!problems || problems.length === 0) {
        problemsList.innerHTML = '<p class="no-results">Nie znaleziono zadań.</p>';
        return;
    }

    problemsList.innerHTML = problems.map(problem => createProblemCard(problem)).join('');
}

function displayPagination() {
    const paginationContainer = document.getElementById('pagination');
    if (!paginationContainer || !paginationData) return;

    const totalPages = Math.ceil(paginationData.count / 20);
    const startItem = (currentPage - 1) * 20 + 1;
    const endItem = Math.min(currentPage * 20, paginationData.count);

    let html = '<div class="pagination-container">';

    // Info
    html += `<div class="pagination-info">Zadania ${startItem}-${endItem} z ${paginationData.count}</div>`;

    html += '<div class="pagination-buttons">';

    // Previous button
    if (paginationData.previous) {
        html += `<button class="btn btn-secondary pagination-btn" onclick="loadProblems(${currentPage - 1})">
            <i class="fas fa-chevron-left"></i> Poprzednia
        </button>`;
    } else {
        html += `<button class="btn btn-secondary pagination-btn" disabled>
            <i class="fas fa-chevron-left"></i> Poprzednia
        </button>`;
    }

    // Page numbers
    html += '<div class="pagination-pages">';

    // Show first page
    if (currentPage > 3) {
        html += `<button class="pagination-page" onclick="loadProblems(1)">1</button>`;
        if (currentPage > 4) {
            html += '<span class="pagination-ellipsis">...</span>';
        }
    }

    // Show pages around current
    for (let i = Math.max(1, currentPage - 2); i <= Math.min(totalPages, currentPage + 2); i++) {
        if (i === currentPage) {
            html += `<button class="pagination-page active">${i}</button>`;
        } else {
            html += `<button class="pagination-page" onclick="loadProblems(${i})">${i}</button>`;
        }
    }

    // Show last page
    if (currentPage < totalPages - 2) {
        if (currentPage < totalPages - 3) {
            html += '<span class="pagination-ellipsis">...</span>';
        }
        html += `<button class="pagination-page" onclick="loadProblems(${totalPages})">${totalPages}</button>`;
    }

    html += '</div>';

    // Next button
    if (paginationData.next) {
        html += `<button class="btn btn-secondary pagination-btn" onclick="loadProblems(${currentPage + 1})">
            Następna <i class="fas fa-chevron-right"></i>
        </button>`;
    } else {
        html += `<button class="btn btn-secondary pagination-btn" disabled>
            Następna <i class="fas fa-chevron-right"></i>
        </button>`;
    }

    html += '</div></div>';

    paginationContainer.innerHTML = html;
}

function createProblemCard(problem) {
    const difficultyClass = problem.difficulty || 'easy';
    const difficultyLabel = getDifficultyLabel(problem.difficulty);
    const isCompleted = problem.is_solved || problem.user_status === 'completed';
    const statusClass = isCompleted ? 'completed' : '';

    // Use acceptance rate from API (already calculated)
    const acceptanceRate = problem.acceptance_rate !== undefined
        ? Math.round(problem.acceptance_rate)
        : 0;

    // Get supported languages and solved languages
    const languages = problem.languages ? problem.languages.split(',') : ['Python', 'JavaScript', 'C#', 'C++'];

    // Language display name mapping
    const languageDisplayNames = {
        'python': 'Python',
        'javascript': 'JavaScript',
        'csharp': 'C#',
        'c#': 'C#',
        'java': 'Java',
        'cpp': 'C++',
        'c': 'C'
    };

    // Normalize language name for comparison (handle C# / csharp / C++ variants)
    const normalizeLanguage = (lang) => {
        const normalized = lang.toLowerCase().trim();
        // Convert all C# variants to 'csharp' for consistent comparison
        if (normalized === 'c#' || normalized === 'csharp' || normalized === 'c-sharp') {
            return 'csharp';
        }
        // Convert all C++ variants to 'cpp' for consistent comparison
        if (normalized === 'c++' || normalized === 'cpp' || normalized === 'cplusplus') {
            return 'cpp';
        }
        return normalized;
    };

    // Get solved languages - API now returns array, but handle string for backward compatibility
    let solvedLanguages = [];
    if (problem.solved_language) {
        if (Array.isArray(problem.solved_language)) {
            // API returns array of solved languages - normalize and remove duplicates
            const normalized = problem.solved_language.map(lang => normalizeLanguage(lang));
            solvedLanguages = [...new Set(normalized)]; // Remove duplicates
        } else {
            // Backward compatibility: single language as string
            solvedLanguages = [normalizeLanguage(problem.solved_language)];
        }
    }

    // Debug: log what we're getting from API
    if (problem.is_solved || problem.solved_language) {
        console.log(`Problem: ${problem.title}`);
        console.log('  is_solved:', problem.is_solved);
        console.log('  solved_language (raw):', problem.solved_language);
        console.log('  solvedLanguages (unique, normalized):', solvedLanguages);
        console.log('  available languages:', problem.languages);
    }

    return `
        <a href="/problems/${problem.slug}/" class="problem-card ${statusClass}">
            <div class="problem-card-header">
                <div style="flex: 1;">
                    <h3>
                        ${isCompleted ? '<i class="fas fa-check-circle completed-icon" style="color: var(--success-color); margin-right: 0.5rem;"></i>' : ''}
                        ${problem.title}
                    </h3>
                    <div class="problem-badges" style="margin-top: 0.75rem;">
                        ${languages.map(lang => {
                            const langLower = lang.trim().toLowerCase();
                            const displayName = languageDisplayNames[langLower] || lang.trim();
                            const normalizedLang = normalizeLanguage(lang);
                            const isSolved = solvedLanguages.includes(normalizedLang);

                            // Debug: log language matching for solved problems
                            if (problem.is_solved || problem.solved_language) {
                                console.log(`  Checking language: ${lang}`);
                                console.log(`    normalized: ${normalizedLang}`);
                                console.log(`    isSolved: ${isSolved}`);
                                console.log(`    solvedLanguages contains: ${solvedLanguages.join(', ')}`);
                            }

                            return `
                                <span class="language-badge ${isSolved ? 'language-solved' : ''}">
                                    <i class="fas fa-code"></i> ${displayName}
                                    ${isSolved ? '<i class="fas fa-check" style="margin-left: 0.25rem; font-size: 0.75rem;"></i>' : ''}
                                </span>
                            `;
                        }).join('')}
                        ${isCompleted ? '<span class="solved-badge" style="margin-left: 0.5rem;">Ukończone</span>' : ''}
                    </div>
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.5rem; align-items: flex-end;">
                    <span class="difficulty-badge difficulty-${difficultyClass}">${difficultyLabel}</span>
                    <span class="points-badge">
                        <i class="fas fa-star"></i> ${problem.points} pkt
                    </span>
                </div>
            </div>

            <div class="problem-card-footer" style="margin-top: 1.25rem;">
                <div style="display: flex; gap: 1.5rem; align-items: center;">
                    <span class="stat-item" style="display: flex; align-items: center; gap: 0.5rem; color: var(--text-secondary); font-size: 0.9rem;">
                        <i class="fas fa-users"></i> ${problem.total_submissions || 0} rozwiązań
                    </span>
                    <span class="problem-acceptance" style="display: flex; align-items: center; gap: 0.5rem;">
                        <i class="fas fa-chart-bar" style="color: ${acceptanceRate > 50 ? 'var(--success-color)' : 'var(--text-secondary)'};"></i>
                        ${acceptanceRate}% akceptacji
                    </span>
                </div>
            </div>
        </a>
    `;
}

// PROBLEM DETAIL PAGE

function renderProblemDescription() {
    const descriptionElement = document.getElementById('problemDescription');
    if (!descriptionElement) return;

    const rawDescription = descriptionElement.textContent || descriptionElement.innerText;

    // Check if marked.js is loaded
    if (typeof marked !== 'undefined' && rawDescription) {
        try {
            const htmlContent = marked.parse(rawDescription);
            descriptionElement.innerHTML = htmlContent;
        } catch (error) {
            console.error('Error rendering markdown:', error);
            // Keep the original text if markdown parsing fails
        }
    }
}

function initProblemDetailPage() {
    // Render problem description as Markdown
    renderProblemDescription();

    // Load test cases
    if (window.PROBLEM_SLUG) {
        loadTestCases(window.PROBLEM_SLUG);
    }

    // Initialize Monaco Editor
    const editorElement = document.getElementById('codeEditor');
    if (editorElement) {
        // Wait for Monaco to be loaded
        const initMonaco = () => {
            if (typeof monaco !== 'undefined') {
                // Get initial code template for Python (default language)
                const initialCode = window.CODE_TEMPLATES?.python || '# Wpisz swój kod tutaj';

                codeEditor = monaco.editor.create(editorElement, {
                    value: initialCode,
                    language: 'python',
                    theme: 'vs-dark',
                    automaticLayout: true,
                    fontSize: 16,
                    lineNumbers: 'on',
                    roundedSelection: false,
                    scrollBeyondLastLine: false,
                    readOnly: false,
                    minimap: {
                        enabled: true
                    },
                    tabSize: 4,
                    insertSpaces: true,
                    wordWrap: 'on',
                    bracketPairColorization: {
                        enabled: true
                    },
                    padding: {
                        top: 10,
                        bottom: 10
                    }
                });

                // Setup event listeners after editor is created
                setupEditorEventListeners();
            } else {
                // Monaco not loaded yet, try again
                setTimeout(initMonaco, 100);
            }
        };

        // Check if require is available
        if (typeof require !== 'undefined' && typeof require.config === 'function') {
            require(['vs/editor/editor.main'], function() {
                initMonaco();
            });
        } else {
            // Fallback: wait for Monaco to load
            setTimeout(initMonaco, 500);
        }
    }
}

function setupEditorEventListeners() {
    // Language select
    const languageSelect = document.getElementById('languageSelect');
    if (languageSelect) {
        languageSelect.addEventListener('change', (e) => {
            changeEditorLanguage(e.target.value);
        });
    }

    // Font size select
    const fontSizeSelect = document.getElementById('fontSizeSelect');
    if (fontSizeSelect) {
        fontSizeSelect.addEventListener('change', (e) => {
            changeEditorFontSize(parseInt(e.target.value));
        });
    }

    // Run code button
    const runCodeBtn = document.getElementById('runCodeBtn');
    if (runCodeBtn) {
        runCodeBtn.addEventListener('click', runCode);
    }

    // Submit code button
    const submitCodeBtn = document.getElementById('submitCodeBtn');
    if (submitCodeBtn) {
        submitCodeBtn.addEventListener('click', submitCode);
    }
}

async function loadTestCases(slug) {
    const headers = {};
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/problems/${slug}/`, { headers });
        const problem = await response.json();

        if (problem.test_cases) {
            displayTestCases(problem.test_cases);
        }
    } catch (error) {
        console.error('Error loading test cases:', error);
    }
}

function displayTestCases(testCases) {
    const testCasesList = document.getElementById('testCasesList');
    if (!testCasesList || !testCases) return;

    testCasesList.innerHTML = testCases.slice(0, 3).map((testCase, index) => {
        // Safely get input and output values
        const inputData = testCase.input_data || testCase.input || '';
        const expectedOutput = testCase.expected_output || testCase.output || '';

        return `
            <div class="test-case">
                <h4>Przykład ${index + 1}</h4>
                <div class="test-case-content">
                    <div>
                        <strong>Wejście:</strong>
                        <pre>${inputData || '(brak danych)'}</pre>
                    </div>
                    <div>
                        <strong>Oczekiwane wyjście:</strong>
                        <pre>${expectedOutput || '(brak danych)'}</pre>
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

function changeEditorLanguage(language) {
    if (!codeEditor) {
        console.error('Code editor not initialized');
        return;
    }

    console.log('Changing language to:', language);
    console.log('Available templates:', window.CODE_TEMPLATES);

    const languageMap = {
        'python': 'python',
        'javascript': 'javascript',
        'csharp': 'csharp',
        'cpp': 'cpp'
    };

    const monacoLanguage = languageMap[language] || 'python';

    // Get the code template for the selected language
    const codeTemplate = window.CODE_TEMPLATES?.[language];
    console.log('Code template for', language, ':', codeTemplate);

    if (!codeTemplate) {
        console.warn('No template found for language:', language);
    }

    // Get current code
    const currentCode = codeEditor.getValue();
    console.log('Current code length:', currentCode.length);

    // Check if current code matches any of the default templates
    const isDefaultTemplate = (code) => {
        const trimmedCode = code.trim();

        // Check if it matches Python template
        if (window.CODE_TEMPLATES?.python && trimmedCode === window.CODE_TEMPLATES.python.trim()) {
            return true;
        }

        // Check if it matches JavaScript template
        if (window.CODE_TEMPLATES?.javascript && trimmedCode === window.CODE_TEMPLATES.javascript.trim()) {
            return true;
        }

        // Check if it matches C# template
        if (window.CODE_TEMPLATES?.csharp && trimmedCode === window.CODE_TEMPLATES.csharp.trim()) {
            return true;
        }

        // Check if it matches C++ template
        if (window.CODE_TEMPLATES?.cpp && trimmedCode === window.CODE_TEMPLATES.cpp.trim()) {
            return true;
        }

        // Check for common template markers
        return trimmedCode.length < 50 ||
               code.includes('Wpisz swój kod tutaj') ||
               (code.includes('def solution():') && code.includes('pass')) ||
               (code.includes('function solution()') && code.includes('// TODO')) ||
               (code.includes('public class Solution') && code.includes('// TODO')) ||
               (code.includes('#include <iostream>') && code.includes('int main()'));
    };

    const shouldReplaceCode = isDefaultTemplate(currentCode);
    console.log('Should replace code:', shouldReplaceCode, '(is default template)');

    if (shouldReplaceCode && codeTemplate) {
        console.log('Setting new code template');
        codeEditor.setValue(codeTemplate);
    } else if (!codeTemplate) {
        console.warn('No template available, keeping current code');
    } else {
        console.log('User has custom code, not replacing');
    }

    // Change syntax highlighting
    const model = codeEditor.getModel();
    if (model && typeof monaco !== 'undefined') {
        monaco.editor.setModelLanguage(model, monacoLanguage);
        console.log('Changed syntax highlighting to:', monacoLanguage);
    }
}

function changeEditorFontSize(fontSize) {
    if (!codeEditor) return;

    codeEditor.updateOptions({
        fontSize: fontSize
    });
}

async function runCode() {
    if (!codeEditor || !window.PROBLEM_SLUG) return;

    const code = codeEditor.getValue();
    const language = document.getElementById('languageSelect')?.value || 'python';

    if (!code.trim()) {
        alert('Proszę wprowadzić kod!');
        return;
    }

    // Show loading state for "Run Code"
    showRunningState('run');

    try {
        const response = await fetch(`${API_BASE_URL}/submissions/create/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authToken}`
            },
            body: JSON.stringify({
                problem_slug: window.PROBLEM_SLUG,
                code: code,
                language: language
            })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            console.error('API Error:', errorData);
            throw new Error('Błąd podczas wysyłania kodu');
        }

        const submission = await response.json();
        pollSubmissionResult(submission.id, 0, 'run');
    } catch (error) {
        console.error('Error running code:', error);
        alert('Błąd podczas uruchamiania kodu. Spróbuj ponownie.');
    }
}

async function submitCode() {
    if (!codeEditor || !window.PROBLEM_SLUG) return;

    const code = codeEditor.getValue();
    const language = document.getElementById('languageSelect')?.value || 'python';

    if (!code.trim()) {
        alert('Proszę wprowadzić kod!');
        return;
    }

    // Show loading state for "Submit Solution"
    showRunningState('submit');

    try {
        const response = await fetch(`${API_BASE_URL}/submissions/create/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authToken}`
            },
            body: JSON.stringify({
                problem_slug: window.PROBLEM_SLUG,
                code: code,
                language: language
            })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            console.error('API Error:', errorData);
            throw new Error('Błąd podczas wysyłania rozwiązania');
        }

        const submission = await response.json();
        pollSubmissionResult(submission.id, 0, 'submit');
    } catch (error) {
        console.error('Error submitting code:', error);
        alert('Błąd podczas wysyłania rozwiązania. Spróbuj ponownie.');
    }
}

async function pollSubmissionResult(submissionId, attempts = 0, submissionType = 'submit') {
    const maxAttempts = 30;

    if (attempts >= maxAttempts) {
        showResults({ status: 'error', message: 'Timeout - sprawdzanie zajęło zbyt długo' }, submissionType);
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/submissions/${submissionId}/`, {
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        });

        const submission = await response.json();

        if (submission.status === 'pending' || submission.status === 'running') {
            setTimeout(() => pollSubmissionResult(submissionId, attempts + 1, submissionType), 1000);
        } else {
            showResults(submission, submissionType);
        }
    } catch (error) {
        console.error('Error polling submission:', error);
        showResults({ status: 'error', message: 'Błąd podczas sprawdzania wyniku' }, submissionType);
    }
}

function showRunningState(submissionType = 'submit') {
    const resultsPanel = document.getElementById('resultsPanel');
    const resultsContent = document.getElementById('resultsContent');

    if (!resultsPanel || !resultsContent) return;

    resultsPanel.style.display = 'block';

    const headerTitle = submissionType === 'run' ? 'Testowanie kodu...' : 'Wysyłanie rozwiązania...';

    resultsContent.innerHTML = `
        <div class="result-header running">
            <div class="result-header-title">
                <h4>${headerTitle}</h4>
            </div>
        </div>
        <div class="running-state">
            <div class="spinner">
                <i class="fas fa-spinner fa-spin"></i>
            </div>
            <p>${submissionType === 'run' ? 'Sprawdzanie na testach przykładowych...' : 'Sprawdzanie na wszystkich testach...'}</p>
        </div>
    `;
}

function showResults(result, submissionType = 'submit') {
    const resultsPanel = document.getElementById('resultsPanel');
    const resultsContent = document.getElementById('resultsContent');

    if (!resultsPanel || !resultsContent) return;

    resultsPanel.style.display = 'block';

    const statusClass = result.status === 'accepted' ? 'success' : 'error';
    const statusLabel = getStatusLabel(result.status);

    // Different header based on submission type
    const headerTitle = submissionType === 'run' ? 'Wynik testowania' : 'Poprawność odpowiedzi';

    let html = `
        <div class="result-header ${statusClass}">
            <div class="result-header-title">
                <h4>${headerTitle}</h4>
            </div>
        </div>
        <div class="result-status-banner ${statusClass}">
            <span>${statusLabel}</span>
        </div>
    `;

    if (result.test_results) {
        html += displayTestResults(result.test_results, submissionType);
    }

    if (result.error_message) {
        html += `<div class="error-message">${result.error_message}</div>`;
    }

    if (result.status === 'accepted') {
        if (submissionType === 'submit') {
            html += `
                <div class="success-message">
                    <div>
                        <strong>Gratulacje! Rozwiązanie zaakceptowane!</strong>
                        <p>Twoje rozwiązanie przeszło wszystkie testy pomyślnie.</p>
                        ${result.points_awarded ? `<div class="points-awarded">Zdobyte punkty: <strong>${result.points_awarded}</strong></div>` : ''}
                    </div>
                </div>
            `;
        } else {
            html += `
                <div class="success-message run-success">
                    <div>
                        <strong>Świetnie! Testy przykładowe zaliczone</strong>
                        <p>Twój kod działa poprawnie na przykładowych testach. Możesz teraz wysłać oficjalne rozwiązanie!</p>
                    </div>
                </div>
            `;
        }
    } else if (submissionType === 'run') {
        html += `
            <div class="info-message">
                <p>To był tylko test na przykładowych danych. Popraw kod i spróbuj ponownie.</p>
            </div>
        `;
    }

    resultsContent.innerHTML = html;
}

function displayTestResults(testResults, submissionType = 'submit') {
    if (!testResults || testResults.length === 0) return '';

    const testTypeLabel = submissionType === 'run' ? 'Wyniki testów przykładowych:' : 'Wyniki wszystkich testów:';

    return `
        <div class="test-results">
            <h4>${testTypeLabel}</h4>
            ${testResults.map((test, index) => {
                const passedClass = test.passed ? 'passed' : 'failed';

                // Check if values look the same but test failed (likely type/whitespace issue)
                const expectedStr = String(test.expected || '').trim();
                const actualStr = String(test.actual || '').trim();
                const valuesLookSame = !test.passed && expectedStr === actualStr;

                return `
                    <div class="test-result ${passedClass}">
                        <div class="test-result-header">
                            <span>Test ${index + 1}</span>
                            <span class="test-status-label">${test.passed ? 'Zaliczony' : 'Niezaliczony'}</span>
                        </div>
                        ${!test.passed ? `
                            <div class="test-result-details">
                                <div class="test-detail-row"><strong>Wejście:</strong> <code>${test.input || 'brak'}</code></div>
                                <div class="test-detail-row"><strong>Oczekiwane:</strong> <code>${test.expected}</code></div>
                                <div class="test-detail-row"><strong>Otrzymano:</strong> <code>${test.actual}</code></div>
                                ${valuesLookSame ? `
                                    <div class="test-warning">
                                        Wartości wyglądają identycznie - możliwy problem z typem danych lub białymi znakami w kodzie sprawdzającym
                                    </div>
                                ` : ''}
                            </div>
                        ` : `
                            <div class="test-success-details">
                                Test przeszedł pomyślnie
                            </div>
                        `}
                    </div>
                `;
            }).join('')}
        </div>
    `;
}

// LEADERBOARD PAGE

function initLeaderboardPage() {
    loadLeaderboard('global');
    loadLeaderboardStats();

    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const tab = btn.dataset.tab;
            loadLeaderboard(tab);
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });
}

async function loadLeaderboardStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/problems/stats/overall/`);
        const data = await response.json();

        const totalUsers = document.getElementById('totalUsers');
        const totalSubmissions = document.getElementById('totalSubmissions');

        if (totalUsers) totalUsers.textContent = data.total_users || 0;
        if (totalSubmissions) totalSubmissions.textContent = data.total_submissions || 0;
    } catch (error) {
        console.error('Error loading leaderboard stats:', error);
    }
}

// Get rank info based on experience points
function getRankByExp(exp) {
    if (exp >= 10000) {
        return { name: 'Code Legend', icon: 'fa-crown', color: '#FFD700' };
    } else if (exp >= 8000) {
        return { name: 'Code Sage', icon: 'fa-scroll', color: '#00BCD4' };
    } else if (exp >= 5000) {
        return { name: 'Tech Mastermind', icon: 'fa-brain', color: '#E91E63' };
    } else if (exp >= 3000) {
        return { name: 'Code Architect', icon: 'fa-drafting-compass', color: '#673AB7' };
    } else if (exp >= 1500) {
        return { name: 'Algorithm Wizard', icon: 'fa-hat-wizard', color: '#2196F3' };
    } else if (exp >= 500) {
        return { name: 'Code Ninja', icon: 'fa-user-ninja', color: '#9C27B0' };
    } else if (exp >= 100) {
        return { name: 'Bug Hunter', icon: 'fa-bug', color: '#FF9800' };
    } else {
        return { name: 'Code Rookie', icon: 'fa-seedling', color: '#8BC34A' };
    }
}

async function loadLeaderboard(type = 'global') {
    const urls = {
        'global': `${API_BASE_URL}/leaderboard/global/`,
        'weekly': `${API_BASE_URL}/leaderboard/weekly/`,
        'solvers': `${API_BASE_URL}/leaderboard/solvers/`
    };

    try {
        const response = await fetch(urls[type]);
        const data = await response.json();
        displayLeaderboard(data, type);
    } catch (error) {
        console.error('Error loading leaderboard:', error);
        const leaderboardContent = document.getElementById('leaderboardContent');
        if (leaderboardContent) {
            leaderboardContent.innerHTML = '<p class="error">Błąd wczytywania rankingu.</p>';
        }
    }
}

function displayLeaderboard(data, type) {
    const leaderboardContent = document.getElementById('leaderboardContent');
    if (!leaderboardContent) return;

    const items = data.results || data;

    if (!items || items.length === 0) {
        leaderboardContent.innerHTML = '<p class="no-results">Brak danych w rankingu.</p>';
        return;
    }

    let html = '';

    // Find max score for progress bars
    const maxScore = Math.max(...items.map(item => {
        if (type === 'global') return item.experience_points || 0;
        if (type === 'weekly') return item.weekly_points || 0;
        if (type === 'solvers') return item.solved_count || 0;
        return 0;
    }));

    items.forEach((item, index) => {
        const rank = index + 1;
        const username = item.username || item.user?.username;

        // Determine rank class and medal
        let rankClass = '';
        let medalHtml = '';
        let rankBadgeClass = '';

        if (rank === 1) {
            rankClass = 'top-1';
            medalHtml = '<i class="fas fa-crown"></i>';
            rankBadgeClass = 'rank-gold';
        } else if (rank === 2) {
            rankClass = 'top-2';
            medalHtml = '<i class="fas fa-medal"></i>';
            rankBadgeClass = 'rank-silver';
        } else if (rank === 3) {
            rankClass = 'top-3';
            medalHtml = '<i class="fas fa-medal"></i>';
            rankBadgeClass = 'rank-bronze';
        }

        // Get user rank based on experience points
        const userExp = item.experience_points || item.total_experience || 0;
        const userRank = getRankByExp(userExp);

        // Calculate score for this user
        let score = 0;
        let scoreLabel = '';
        let scoreUnit = '';
        let extraInfo = '';
        if (type === 'global') {
            score = item.experience_points || 0;
            scoreLabel = `${score}`;
            scoreUnit = 'pkt';
            extraInfo = `${item.solved_count || 0} rozwiązań`;
        } else if (type === 'weekly') {
            score = item.weekly_points || 0;
            scoreLabel = `${score}`;
            scoreUnit = 'pkt';
            extraInfo = 'w tym tygodniu';
        } else if (type === 'solvers') {
            score = item.solved_count || 0;
            scoreLabel = `${score}`;
            scoreUnit = '';
            extraInfo = 'rozwiązanych zadań';
        }

        html += `
            <div class="leaderboard-card ${rankClass}">
                <div class="leaderboard-card-rank ${rankBadgeClass}">
                    ${medalHtml}
                    <span class="rank-number">#${rank}</span>
                </div>

                <div class="leaderboard-card-user">
                    <div class="user-avatar" style="border-color: ${userRank.color}; box-shadow: 0 4px 12px ${userRank.color}40;">
                        <i class="fas ${userRank.icon}" style="color: ${userRank.color};"></i>
                    </div>
                    <div class="user-info">
                        <div class="user-name">${username}</div>
                        ${type === 'global' ? `<div class="user-level">Poziom ${item.level || 1}</div>` : ''}
                    </div>
                </div>

                <div class="leaderboard-card-stats">
                    <div class="score-info">
                        <div>
                            <span class="score-label">${scoreLabel}</span>
                            ${scoreUnit ? `<span class="score-unit"> ${scoreUnit}</span>` : ''}
                        </div>
                        <span class="extra-stat">${extraInfo}</span>
                    </div>
                </div>
            </div>
        `;
    });

    leaderboardContent.innerHTML = html;
}

// PROFILE PAGE

function initProfilePage() {
    if (!authToken) {
        window.location.href = '/';
        return;
    }

    loadProfile();
}

async function loadProfile() {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/profile/`, {
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        });

        const profile = await response.json();
        displayProfile(profile);
    } catch (error) {
        console.error('Error loading profile:', error);
        const profileContent = document.getElementById('profileContent');
        if (profileContent) {
            profileContent.innerHTML = '<p class="error">Błąd wczytywania profilu.</p>';
        }
    }
}

function displayProfile(profile) {
    const profileContent = document.getElementById('profileContent');
    if (!profileContent) return;

    const user = profile.user || currentUser;

    // Calculate level progress
    const currentLevel = profile.level || 1;
    const currentXP = profile.experience_points || 0;
    const xpForCurrentLevel = currentLevel * 100;
    const xpForNextLevel = (currentLevel + 1) * 100;
    const xpProgress = currentXP - xpForCurrentLevel;
    const xpNeeded = xpForNextLevel - xpForCurrentLevel;
    const progressPercent = Math.min((xpProgress / xpNeeded) * 100, 100);

    // Get current and next rank
    const currentRank = getRankByExp(currentXP);
    const rankThresholds = [
        { name: 'Code Rookie', threshold: 0, icon: 'fa-seedling', color: '#8BC34A' },
        { name: 'Bug Hunter', threshold: 100, icon: 'fa-bug', color: '#FF9800' },
        { name: 'Code Ninja', threshold: 500, icon: 'fa-user-ninja', color: '#9C27B0' },
        { name: 'Algorithm Wizard', threshold: 1500, icon: 'fa-hat-wizard', color: '#2196F3' },
        { name: 'Code Architect', threshold: 3000, icon: 'fa-drafting-compass', color: '#673AB7' },
        { name: 'Tech Mastermind', threshold: 5000, icon: 'fa-brain', color: '#E91E63' },
        { name: 'Code Sage', threshold: 8000, icon: 'fa-scroll', color: '#00BCD4' },
        { name: 'Code Legend', threshold: 10000, icon: 'fa-crown', color: '#FFD700' }
    ];

    // Find next rank
    let nextRank = null;
    let rankProgress = 0;
    let rankXpNeeded = 0;
    let rankXpProgress = 0;

    for (let i = 0; i < rankThresholds.length; i++) {
        if (currentXP < rankThresholds[i].threshold) {
            nextRank = rankThresholds[i];
            const currentRankThreshold = i > 0 ? rankThresholds[i - 1].threshold : 0;
            rankXpProgress = currentXP - currentRankThreshold;
            rankXpNeeded = nextRank.threshold - currentRankThreshold;
            rankProgress = (rankXpProgress / rankXpNeeded) * 100;
            break;
        }
    }

    // If max rank (Code Legend)
    if (!nextRank) {
        nextRank = { name: 'Code Legend', threshold: 10000, icon: 'fa-crown', color: '#FFD700' };
        rankProgress = 100;
        rankXpProgress = currentXP - 10000;
        rankXpNeeded = 0;
    }

    const html = `
        <div class="profile-header-card">
            <div class="profile-header-bg-pattern"></div>
            <div class="profile-header-content">
                <div class="profile-avatar-large">
                    ${user.username ? user.username[0].toUpperCase() : 'U'}
                </div>
                <div class="profile-info">
                    <h2 class="profile-username">${user.username}</h2>
                    <p class="profile-email"><i class="fas fa-envelope"></i> ${user.email}</p>
                </div>
            </div>
        </div>

        <!-- Rank Progress -->
        <div class="rank-progress-card">
            <div class="rank-progress-header">
                <div class="current-rank-display">
                    <div class="rank-icon-wrapper" style="background: ${currentRank.color}20; border: 2px solid ${currentRank.color};">
                        <i class="fas ${currentRank.icon}" style="color: ${currentRank.color};"></i>
                    </div>
                    <div class="rank-text-info">
                        <div class="rank-label">Aktualna ranga</div>
                        <div class="rank-name" style="color: ${currentRank.color};">${currentRank.name}</div>
                    </div>
                </div>
                ${rankProgress < 100 ? `
                    <div class="next-rank-display">
                        <div class="rank-icon-wrapper small" style="background: ${nextRank.color}20; border: 2px solid ${nextRank.color};">
                            <i class="fas ${nextRank.icon}" style="color: ${nextRank.color};"></i>
                        </div>
                        <div class="rank-text-info">
                            <div class="rank-label">Następna ranga</div>
                            <div class="rank-name" style="color: ${nextRank.color};">${nextRank.name}</div>
                        </div>
                    </div>
                ` : `
                    <div class="max-rank-badge">
                        <i class="fas fa-star"></i>
                        <span>Maksymalna ranga!</span>
                    </div>
                `}
            </div>
            ${rankProgress < 100 ? `
                <div class="rank-progress-bar-wrapper">
                    <div class="rank-progress-bar">
                        <div class="rank-progress-fill" style="width: ${rankProgress}%; background: linear-gradient(90deg, ${currentRank.color}, ${nextRank.color}); box-shadow: 0 0 20px ${nextRank.color}40;">
                            <span class="rank-progress-label">${Math.round(rankProgress)}%</span>
                        </div>
                    </div>
                    <div class="rank-progress-text">
                        <span style="color: ${nextRank.color}; font-weight: 600;">${rankXpNeeded - rankXpProgress} EXP</span> do <strong>${nextRank.name}</strong>
                    </div>
                    <div class="rank-progress-details">
                        ${rankXpProgress} / ${rankXpNeeded} EXP
                    </div>
                </div>
            ` : `
                <div class="rank-progress-max">
                    <div class="rank-progress-text">
                        <i class="fas fa-trophy" style="color: ${currentRank.color};"></i>
                        Osiągnąłeś najwyższą rangę w systemie!
                    </div>
                    <div class="rank-progress-details">
                        Łączne EXP: ${currentXP}
                    </div>
                </div>
            `}
        </div>

        <!-- Main Stats -->
        <div class="profile-stats-grid">
            <div class="profile-stat-card stat-xp">
                <div class="profile-stat-icon" style="color: #FFD700;"><i class="fas fa-star"></i></div>
                <div class="profile-stat-value">${currentXP}</div>
                <div class="profile-stat-label">Punkty XP</div>
            </div>
            <div class="profile-stat-card stat-solved">
                <div class="profile-stat-icon" style="color: #10B981;"><i class="fas fa-check-circle"></i></div>
                <div class="profile-stat-value">${profile.solved_count || 0}</div>
                <div class="profile-stat-label">Rozwiązane zadania</div>
            </div>
            <div class="profile-stat-card stat-submissions">
                <div class="profile-stat-icon" style="color: #3B82F6;"><i class="fas fa-code-branch"></i></div>
                <div class="profile-stat-value">${profile.total_submissions || 0}</div>
                <div class="profile-stat-label">Wszystkie próby</div>
            </div>
        </div>

        <!-- Difficulty Breakdown -->
        <div class="profile-section">
            <h3><i class="fas fa-chart-bar"></i> Zadania według trudności</h3>
            <div class="difficulty-breakdown-grid">
                <div class="difficulty-card difficulty-easy-card">
                    <div class="difficulty-card-icon">
                        <i class="fas fa-smile"></i>
                    </div>
                    <div class="difficulty-card-content">
                        <div class="difficulty-card-label">Łatwe</div>
                        <div class="difficulty-card-value">${profile.easy_solved || 0}</div>
                        <div class="difficulty-card-subtitle">rozwiązanych</div>
                    </div>
                </div>

                <div class="difficulty-card difficulty-medium-card">
                    <div class="difficulty-card-icon">
                        <i class="fas fa-meh"></i>
                    </div>
                    <div class="difficulty-card-content">
                        <div class="difficulty-card-label">Średnie</div>
                        <div class="difficulty-card-value">${profile.medium_solved || 0}</div>
                        <div class="difficulty-card-subtitle">rozwiązanych</div>
                    </div>
                </div>

                <div class="difficulty-card difficulty-hard-card">
                    <div class="difficulty-card-icon">
                        <i class="fas fa-fire"></i>
                    </div>
                    <div class="difficulty-card-content">
                        <div class="difficulty-card-label">Trudne</div>
                        <div class="difficulty-card-value">${profile.hard_solved || 0}</div>
                        <div class="difficulty-card-subtitle">rozwiązanych</div>
                    </div>
                </div>
            </div>
        </div>
    `;

    profileContent.innerHTML = html;
}

function displayRecentActivity(submissions) {
    if (!submissions || submissions.length === 0) {
        return `
            <div class="empty-state">
                <i class="fas fa-inbox"></i>
                <p>Brak ostatnich aktywności</p>
                <span>Rozpocznij rozwiązywanie zadań, aby zobaczyć swoją historię</span>
            </div>
        `;
    }

    return submissions.slice(0, 10).map(submission => {
        const isAccepted = submission.status === 'accepted';
        const statusIcon = isAccepted ? 'fa-check-circle' : 'fa-times-circle';
        const statusColor = isAccepted ? '#10B981' : '#EF4444';
        const date = new Date(submission.created_at);
        const formattedDate = date.toLocaleDateString('pl-PL', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });

        return `
            <div class="activity-item ${isAccepted ? 'activity-success' : 'activity-failed'}">
                <div class="activity-icon" style="color: ${statusColor};">
                    <i class="fas ${statusIcon}"></i>
                </div>
                <div class="activity-content">
                    <a href="/problems/${submission.problem_slug}/" class="activity-title">
                        ${submission.problem_title}
                    </a>
                    <div class="activity-meta">
                        <span class="activity-status" style="color: ${statusColor};">
                            ${getStatusLabel(submission.status)}
                        </span>
                        <span class="activity-separator">•</span>
                        <span class="activity-date">
                            <i class="fas fa-clock"></i> ${formattedDate}
                        </span>
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

// AUTHENTICATION

async function checkAuth() {
    if (!authToken) {
        updateAuthUI(false);
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/auth/me/`, {
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        });

        if (response.ok) {
            currentUser = await response.json();
            updateAuthUI(true);
        } else {
            localStorage.removeItem('authToken');
            authToken = null;
            updateAuthUI(false);
        }
    } catch (error) {
        console.error('Error checking auth:', error);
        updateAuthUI(false);
    }
}

function updateAuthUI(isAuthenticated) {
    const loginBtn = document.getElementById('loginBtn');
    const registerBtn = document.getElementById('registerBtn');
    const logoutBtn = document.getElementById('logoutBtn');
    const problemsLink = document.getElementById('problemsLink');
    const userProfileLink = document.getElementById('userProfileLink');
    const usernameDisplay = document.getElementById('usernameDisplay');

    if (isAuthenticated) {
        if (loginBtn) loginBtn.style.display = 'none';
        if (registerBtn) registerBtn.style.display = 'none';
        if (logoutBtn) {
            logoutBtn.style.display = 'inline-block';
            logoutBtn.textContent = 'Wyloguj';
        }
        if (problemsLink) problemsLink.style.display = 'inline-block';
        if (userProfileLink) {
            userProfileLink.style.display = 'flex';
            if (usernameDisplay && currentUser) {
                usernameDisplay.textContent = currentUser.username;
            }
        }
    } else {
        if (loginBtn) loginBtn.style.display = 'inline-block';
        if (registerBtn) registerBtn.style.display = 'inline-block';
        if (logoutBtn) logoutBtn.style.display = 'none';
        if (problemsLink) problemsLink.style.display = 'none';
        if (userProfileLink) userProfileLink.style.display = 'none';
    }
}

async function handleLogin(e) {
    e.preventDefault();

    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    const errorDiv = document.getElementById('loginError');

    try {
        const response = await fetch(`${API_BASE_URL}/auth/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            authToken = data.access;
            localStorage.setItem('authToken', authToken);
            currentUser = data.user;

            hideModal();
            updateAuthUI(true);

            // Redirect to problems page
            window.location.href = '/problems/';
        } else {
            errorDiv.textContent = data.detail || 'Nieprawidłowa nazwa użytkownika lub hasło';
        }
    } catch (error) {
        console.error('Login error:', error);
        errorDiv.textContent = 'Błąd podczas logowania. Spróbuj ponownie.';
    }
}

async function handleRegister(e) {
    e.preventDefault();

    const usernameInput = document.getElementById('registerUsername');
    const emailInput = document.getElementById('registerEmail');
    const passwordInput = document.getElementById('registerPassword');
    const passwordConfirmInput = document.getElementById('registerPasswordConfirm');
    const errorDiv = document.getElementById('registerError');

    const username = usernameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value;
    const passwordConfirm = passwordConfirmInput.value;

    // Clear previous errors
    errorDiv.textContent = '';
    [usernameInput, emailInput, passwordInput, passwordConfirmInput].forEach(input => {
        input.classList.remove('invalid', 'valid');
    });

    // Validate all fields are filled
    let hasError = false;

    if (!username) {
        usernameInput.classList.add('invalid');
        errorDiv.textContent = 'Nazwa użytkownika jest wymagana';
        hasError = true;
    } else {
        usernameInput.classList.add('valid');
    }

    if (!email) {
        emailInput.classList.add('invalid');
        if (!hasError) errorDiv.textContent = 'Email jest wymagany';
        hasError = true;
    } else if (!email.includes('@')) {
        emailInput.classList.add('invalid');
        if (!hasError) errorDiv.textContent = 'Nieprawidłowy format email';
        hasError = true;
    } else {
        emailInput.classList.add('valid');
    }

    if (!password) {
        passwordInput.classList.add('invalid');
        if (!hasError) errorDiv.textContent = 'Hasło jest wymagane';
        hasError = true;
    } else if (password.length < 8) {
        passwordInput.classList.add('invalid');
        if (!hasError) errorDiv.textContent = 'Hasło musi mieć co najmniej 8 znaków';
        hasError = true;
    } else {
        passwordInput.classList.add('valid');
    }

    if (!passwordConfirm) {
        passwordConfirmInput.classList.add('invalid');
        if (!hasError) errorDiv.textContent = 'Potwierdzenie hasła jest wymagane';
        hasError = true;
    } else if (password !== passwordConfirm) {
        passwordInput.classList.add('invalid');
        passwordConfirmInput.classList.add('invalid');
        if (!hasError) errorDiv.textContent = 'Hasła nie są identyczne';
        hasError = true;
    } else {
        passwordConfirmInput.classList.add('valid');
    }

    // Validate privacy policy checkbox
    const privacyCheckbox = document.getElementById('privacyAcceptCheckbox');
    if (privacyCheckbox && !privacyCheckbox.checked) {
        if (!hasError) errorDiv.textContent = 'Musisz zaakceptować Politykę Prywatności';
        hasError = true;
    }

    if (hasError) {
        return;
    }

    try {
        const requestBody = { username, email, password, password_confirm: passwordConfirm };
        console.log('Sending registration request:', requestBody);

        const response = await fetch(`${API_BASE_URL}/auth/register/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        console.log('Response status:', response.status);
        const data = await response.json();
        console.log('Response data:', data);

        if (response.ok) {
            authToken = data.tokens.access;
            localStorage.setItem('authToken', authToken);
            currentUser = data.user;

            hideModal();
            updateAuthUI(true);

            // Redirect to problems page
            window.location.href = '/problems/';
        } else {
            // Handle field-specific errors
            if (data.username) {
                usernameInput.classList.add('invalid');
                errorDiv.textContent = Array.isArray(data.username) ? data.username[0] : data.username;
            }
            if (data.email) {
                emailInput.classList.add('invalid');
                if (!errorDiv.textContent) {
                    errorDiv.textContent = Array.isArray(data.email) ? data.email[0] : data.email;
                }
            }
            if (data.password) {
                passwordInput.classList.add('invalid');
                if (!errorDiv.textContent) {
                    errorDiv.textContent = Array.isArray(data.password) ? data.password[0] : data.password;
                }
            }
            if (data.password_confirm) {
                passwordConfirmInput.classList.add('invalid');
                if (!errorDiv.textContent) {
                    errorDiv.textContent = Array.isArray(data.password_confirm) ? data.password_confirm[0] : data.password_confirm;
                }
            }

            // If no specific field error, show general error
            if (!errorDiv.textContent) {
                const errors = [];
                for (const [field, messages] of Object.entries(data)) {
                    if (Array.isArray(messages)) {
                        errors.push(...messages);
                    } else {
                        errors.push(messages);
                    }
                }
                errorDiv.textContent = errors.join(', ') || 'Błąd podczas rejestracji';
            }

            console.error('Registration failed:', data);
        }
    } catch (error) {
        console.error('Registration error:', error);
        errorDiv.textContent = 'Błąd podczas rejestracji. Spróbuj ponownie.';
    }
}

function logout() {
    localStorage.removeItem('authToken');
    authToken = null;
    currentUser = null;
    window.location.href = '/';
}

function showModal(tab = 'login') {
    const modal = document.getElementById('authModal');
    if (modal) {
        modal.style.display = 'flex';
        switchAuthTab(tab);
    }
}

function hideModal() {
    const modal = document.getElementById('authModal');
    if (modal) {
        modal.style.display = 'none';
    }

    // Clear form errors
    const loginError = document.getElementById('loginError');
    const registerError = document.getElementById('registerError');
    if (loginError) loginError.textContent = '';
    if (registerError) registerError.textContent = '';
}

function switchAuthTab(tabName) {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const tabs = document.querySelectorAll('.modal-tab');

    tabs.forEach(tab => {
        if (tab.dataset.tab === tabName) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });

    if (tabName === 'login') {
        if (loginForm) loginForm.style.display = 'flex';
        if (registerForm) registerForm.style.display = 'none';
    } else {
        if (loginForm) loginForm.style.display = 'none';
        if (registerForm) registerForm.style.display = 'flex';
    }
}

// UTILITY FUNCTIONS

function getDifficultyLabel(difficulty) {
    const labels = {
        'easy': 'Łatwe',
        'medium': 'Średnie',
        'hard': 'Trudne'
    };
    // Convert to lowercase to handle both 'Easy' and 'easy'
    const normalizedDifficulty = difficulty ? difficulty.toLowerCase() : 'easy';
    return labels[normalizedDifficulty] || difficulty;
}

function getStatusLabel(status) {
    const labels = {
        'pending': 'Oczekuje',
        'running': 'Sprawdzanie...',
        'accepted': 'Zaakceptowane',
        'wrong_answer': 'Nieprawidłowa odpowiedź',
        'time_limit_exceeded': 'Przekroczono limit czasu',
        'memory_limit_exceeded': 'Przekroczono limit pamięci',
        'runtime_error': 'Błąd wykonania',
        'compilation_error': 'Błąd kompilacji',
        'error': 'Błąd'
    };
    return labels[status] || status;
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}
