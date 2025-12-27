#!/usr/bin/env node
/**
 * JavaScript sandbox runner for executing user code safely.
 */

const vm = require('vm');
const fs = require('fs');

/**
 * Run user code in sandboxed environment
 */
function runCode(code, testInput) {
    try {
        // Parse test input
        let inputData;
        try {
            inputData = JSON.parse(testInput);
        } catch {
            inputData = testInput;
        }

        // Create sandbox context with limited globals
        const sandbox = {
            console: console,
            inputData: inputData,
            Math: Math,
            JSON: JSON,
            Array: Array,
            Object: Object,
            String: String,
            Number: Number,
            Boolean: Boolean,
            Date: Date,
            parseInt: parseInt,
            parseFloat: parseFloat,
            isNaN: isNaN,
            isFinite: isFinite,
        };

        // Set timeout
        const timeLimit = parseInt(process.env.TIME_LIMIT || '2000');

        // Execute code in sandbox
        const script = new vm.Script(code);
        const context = vm.createContext(sandbox);

        script.runInContext(context, {
            timeout: timeLimit,
            displayErrors: true
        });

    } catch (error) {
        if (error.code === 'ERR_SCRIPT_EXECUTION_TIMEOUT') {
            console.error('Time limit exceeded');
            process.exit(124);
        } else {
            console.error(`Error: ${error.name}: ${error.message}`);
            process.exit(1);
        }
    }
}

/**
 * Main entry point
 */
function main() {
    try {
        // Read code from stdin or environment
        let code = '';

        if (process.stdin.isTTY) {
            code = process.env.CODE || '';
        } else {
            // Read from stdin
            const chunks = [];
            process.stdin.on('data', chunk => chunks.push(chunk));
            process.stdin.on('end', () => {
                code = Buffer.concat(chunks).toString('utf-8');
                executeCode(code);
            });
            return;
        }

        executeCode(code);

    } catch (error) {
        console.error(`Runtime error: ${error.message}`);
        process.exit(1);
    }
}

function executeCode(code) {
    const testInput = process.env.TEST_INPUT || '';
    runCode(code, testInput);
}

// Run main
main();
