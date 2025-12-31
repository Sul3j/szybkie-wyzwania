#!/usr/bin/env python
"""
COMPLETE DEPLOYMENT SCRIPT FOR SZYBKIE WYZWANIA PROBLEMS
This script contains ALL 204+ problems with complete data:
- Descriptions
- Test cases
- Function signatures
- Points (doubled)
- All metadata

Generated: 2025-12-22
Total problems: 206
Total points: 11580

Usage:
    python all_problems.py

Or in Docker:
    docker exec szybkie-wyzwania-web-1 python all_problems.py
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'szybkie_wyzwania_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils.text import slugify
from apps.problems.models import Problem, TestCase, ProblemTag


def main():
    print("=" * 80)
    print("🚀 COMPLETE DEPLOYMENT OF ALL SZYBKIE WYZWANIA PROBLEMS")
    print("=" * 80)

    # Get or create admin user
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@szybkie-wyzwania.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("✅ Created admin user")
    else:
        admin_user = User.objects.filter(is_superuser=True).first() or admin_user
        print("✅ Using existing admin user")

    # Create tags
    print("\n📋 Creating tags...")
    tags_data = [
        {'name': 'Tablice', 'slug': 'arrays'},
        {'name': 'Ciągi znaków', 'slug': 'strings'},
        {'name': 'Matematyka', 'slug': 'math'},
        {'name': 'Algorytmy', 'slug': 'algorithms'},
        {'name': 'Struktury danych', 'slug': 'data-structures'},
    ]

    tags = {}
    for tag_data in tags_data:
        tag, created = ProblemTag.objects.get_or_create(**tag_data)
        tags[tag_data['slug']] = tag
        if created:
            print(f"  ✅ Created tag: {tag.name}")

    # Problems data
    print("\n📦 Loading problems data...")
    problems_data = [
        {
            'title': '''Suma dwóch liczb''',
            'description': '''Napisz funkcję, która zwraca sumę dwóch liczb całkowitych.

**Przykład:**
- Wejście: a = 5, b = 3
- Wyjście: 8

- Wejście: a = -1, b = 10
- Wyjście: 9

**Ograniczenia:**
- -10^9 <= a, b <= 10^9''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def add(a, b):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function add(a, b) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int Add(int a, int b)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto add(auto a, auto b) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "5, 3",
"expected_output": "8",
"is_hidden": False
},
{
"input_data": "-1, 10",
"expected_output": "9",
"is_hidden": False
},
{
"input_data": "0, 0",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "100, -50",
"expected_output": "50",
"is_hidden": True
}
],
            'tags': [],
        },
        {
            'title': '''Odwróć ciąg znaków''',
            'description': '''Napisz funkcję, która odwraca podany ciąg znaków.

**Przykład:**
- Wejście: "hello"
- Wyjście: "olleh"

- Wejście: "Python"
- Wyjście: "nohtyP"

**Ograniczenia:**
- 1 <= długość ciągu <= 10^4''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def reverse_string(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function reverseString(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static string ReverseString(string s)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto reverseString(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello",
"expected_output": "olleh",
"is_hidden": False
},
{
"input_data": "Python",
"expected_output": "nohtyP",
"is_hidden": False
},
{
"input_data": "a",
"expected_output": "a",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Liczba Fibonacciego''',
            'description': '''Oblicz n-tą liczbę Fibonacciego.

Ciąg Fibonacciego definiowany jest jako:
F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) dla n > 1

**Przykład:**
- Wejście: n = 5
- Wyjście: 5
- Wyjaśnienie: F(5) = F(4) + F(3) = 3 + 2 = 5

**Ograniczenia:**
- 0 <= n <= 30''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def fibonacci(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function fibonacci(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int Fibonacci(int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto fibonacci(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "0",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "5",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "10",
"expected_output": "55",
"is_hidden": True
}
],
            'tags': ["algorithms", "math"],
        },
        {
            'title': '''Znajdź element w posortowanej tablicy''',
            'description': '''Zaimplementuj wyszukiwanie binarne, aby znaleźć element w posortowanej tablicy.

Zwróć indeks elementu lub -1, jeśli element nie istnieje.

**Przykład:**
- Wejście: arr = [1, 3, 5, 7, 9], target = 5
- Wyjście: 2

- Wejście: arr = [1, 3, 5, 7, 9], target = 6
- Wyjście: -1

**Ograniczenia:**
- 1 <= długość tablicy <= 10^4
- Wszystkie elementy są unikalne
- Tablica jest posortowana rosnąco''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def binary_search(arr, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function binarySearch(arr, target) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int BinarySearch(int[] arr, int target)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto binarySearch(const vector<int>& arr, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 3, 5, 7, 9], 5",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1, 3, 5, 7, 9], 6",
"expected_output": "-1",
"is_hidden": False
},
{
"input_data": "[1, 2, 3], 1",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Sortowanie bąbelkowe''',
            'description': '''Zaimplementuj algorytm sortowania bąbelkowego.

Posortuj tablicę liczb całkowitych rosnąco.

**Przykład:**
- Wejście: [64, 34, 25, 12, 22, 11, 90]
- Wyjście: [11, 12, 22, 25, 34, 64, 90]

**Ograniczenia:**
- 1 <= długość tablicy <= 1000
- -10^6 <= element <= 10^6''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def bubble_sort(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function bubbleSort(arr) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] BubbleSort(int[] arr)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

void bubbleSort(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[64, 34, 25, 12, 22, 11, 90]",
"expected_output": "[11, 12, 22, 25, 34, 64, 90]",
"is_hidden": False
},
{
"input_data": "[5, 2, 8, 1, 9]",
"expected_output": "[1, 2, 5, 8, 9]",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "[1]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''FizzBuzz''',
            'description': '''Napisz funkcję FizzBuzz dla liczby n.

Dla liczb od 1 do n zwróć tablicę stringów gdzie:
- Dla liczb podzielnych przez 3 i 5: "FizzBuzz"
- Dla liczb podzielnych przez 3: "Fizz"
- Dla liczb podzielnych przez 5: "Buzz"
- W przeciwnym wypadku: string z tą liczbą

**Przykład:**
- Wejście: n = 15
- Wyjście: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

**Ograniczenia:**
- 1 <= n <= 10^4''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def fizz_buzz(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function fizzBuzz(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static string[] FizzBuzz(int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto fizzBuzz(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "3",
"expected_output": "[\"1\", \"2\", \"Fizz\"]",
"is_hidden": False
},
{
"input_data": "5",
"expected_output": "[\"1\", \"2\", \"Fizz\", \"4\", \"Buzz\"]",
"is_hidden": False
},
{
"input_data": "15",
"expected_output": "[\"1\", \"2\", \"Fizz\", \"4\", \"Buzz\", \"Fizz\", \"7\", \"8\", \"Fizz\", \"Buzz\", \"11\", \"Fizz\", \"13\", \"14\", \"FizzBuzz\"]",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Sprawdź palindrom''',
            'description': '''Sprawdź czy podany ciąg znaków jest palindromem.

Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej jest takie samo.
Ignoruj wielkość liter i znaki niealfanumeryczne.

**Przykład:**
- Wejście: "A man, a plan, a canal: Panama"
- Wyjście: true

- Wejście: "race a car"
- Wyjście: false

**Ograniczenia:**
- 1 <= długość ciągu <= 2 * 10^5''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def is_palindrome(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isPalindrome(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static bool IsPalindrome(string s)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isPalindrome(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "A man, a plan, a canal: Panama",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "race a car",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": " ",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Największy wspólny dzielnik''',
            'description': '''Oblicz największy wspólny dzielnik (NWD) dwóch liczb.

NWD to największa liczba, która dzieli obie liczby bez reszty.

**Przykład:**
- Wejście: a = 48, b = 18
- Wyjście: 6

- Wejście: a = 54, b = 24
- Wyjście: 6

**Ograniczenia:**
- 1 <= a, b <= 10^9''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def gcd(a, b):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function gcd(a, b) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int Gcd(int a, int b)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto gcd(auto a, auto b) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "48, 18",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "54, 24",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "1, 1",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "100, 50",
"expected_output": "50",
"is_hidden": True
}
],
            'tags': ["algorithms", "math"],
        },
        {
            'title': '''Dwa elementy o danej sumie''',
            'description': '''Znajdź dwa indeksy w tablicy, których elementy sumują się do podanej liczby.

Zwróć tablicę z dwoma indeksami. Każdy element może być użyty tylko raz.

**Przykład:**
- Wejście: nums = [2, 7, 11, 15], target = 9
- Wyjście: [0, 1]
- Wyjaśnienie: nums[0] + nums[1] = 2 + 7 = 9

**Ograniczenia:**
- 2 <= długość tablicy <= 10^4
- -10^9 <= nums[i] <= 10^9
- Tylko jedno poprawne rozwiązanie istnieje''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def two_sum(nums, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function twoSum(nums, target) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] TwoSum(int[] nums, int target)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> twoSum(const vector<int>& nums, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2, 7, 11, 15], 9",
"expected_output": "[0, 1]",
"is_hidden": False
},
{
"input_data": "[3, 2, 4], 6",
"expected_output": "[1, 2]",
"is_hidden": False
},
{
"input_data": "[3, 3], 6",
"expected_output": "[0, 1]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Walidacja nawiasów''',
            'description': '''Sprawdź czy nawiasy w ciągu znaków są poprawnie zbalansowane.

Ciąg zawiera tylko nawiasy: '(', ')', '{', '}', '[', ']'.

**Przykład:**
- Wejście: "()"
- Wyjście: true

- Wejście: "()[]{}"
- Wyjście: true

- Wejście: "(]"
- Wyjście: false

**Ograniczenia:**
- 1 <= długość ciągu <= 10^4''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_valid(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isValid(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static bool IsValid(string s)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isValid(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "()",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "()[]{}",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "(]",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "([)]",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["strings", "data-structures"],
        },
        {
            'title': '''Maksymalna podtablica''',
            'description': '''Znajdź ciągłą podtablicę o największej sumie i zwróć tę sumę.

**Przykład:**
- Wejście: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
- Wyjście: 6
- Wyjaśnienie: [4, -1, 2, 1] ma największą sumę = 6

**Ograniczenia:**
- 1 <= długość tablicy <= 10^5
- -10^4 <= nums[i] <= 10^4''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_subarray(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maxSubarray(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int MaxSubarray(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxSubarray(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[-2, 1, -3, 4, -1, 2, 1, -5, 4]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[5, 4, -1, 7, 8]",
"expected_output": "23",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Sortowanie przez scalanie''',
            'description': '''Zaimplementuj algorytm sortowania przez scalanie (merge sort).

Posortuj tablicę liczb całkowitych rosnąco używając algorytmu merge sort.

**Przykład:**
- Wejście: [38, 27, 43, 3, 9, 82, 10]
- Wyjście: [3, 9, 10, 27, 38, 43, 82]

**Ograniczenia:**
- 1 <= długość tablicy <= 5 * 10^4
- -10^9 <= element <= 10^9''',
            'difficulty': '''hard''',
            'points': 120,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def merge_sort(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function mergeSort(arr) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] MergeSort(int[] arr)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

void mergeSort(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[38, 27, 43, 3, 9, 82, 10]",
"expected_output": "[3, 9, 10, 27, 38, 43, 82]",
"is_hidden": False
},
{
"input_data": "[5, 2, 8, 1, 9]",
"expected_output": "[1, 2, 5, 8, 9]",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "[1]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Najdłuższy wspólny prefiks''',
            'description': '''Znajdź najdłuższy wspólny prefiks w tablicy ciągów znaków.

Jeśli nie ma wspólnego prefiksu, zwróć pusty ciąg "".

**Przykład:**
- Wejście: ["flower", "flow", "flight"]
- Wyjście: "fl"

- Wejście: ["dog", "racecar", "car"]
- Wyjście: ""

**Ograniczenia:**
- 1 <= długość tablicy <= 200
- 0 <= długość ciągu <= 200''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def longest_common_prefix(strs):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longestCommonPrefix(strs) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static string LongestCommonPrefix(string[] strs)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> longestCommonPrefix(const vector<string>& strs) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[\"flower\", \"flow\", \"flight\"]",
"expected_output": "fl",
"is_hidden": False
},
{
"input_data": "[\"dog\", \"racecar\", \"car\"]",
"expected_output": "",
"is_hidden": False
},
{
"input_data": "[\"ab\", \"a\"]",
"expected_output": "a",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Liczba pierwsza''',
            'description': '''Sprawdź czy podana liczba jest liczbą pierwszą.

Liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki: 1 i samą siebie.

**Przykład:**
- Wejście: 7
- Wyjście: true

- Wejście: 4
- Wyjście: false

**Ograniczenia:**
- 1 <= n <= 10^8''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def is_prime(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isPrime(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static bool IsPrime(int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isPrime(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "7",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "4",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "2",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Znajdź minimum w tablicy''',
            'description': '''Napisz funkcję, która znajduje najmniejszy element w tablicy liczb całkowitych.

**Przykład:**
```
Input: [3, 1, 4, 1, 5, 9, 2, 6]
Output: 1
```

**Ograniczenia:**
- Tablica zawiera co najmniej 1 element
- Wszystkie liczby są całkowite''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_min(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function find_min(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Find_min(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findMin(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3, 1, 4, 1, 5, 9, 2, 6]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[5]",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "[-10, -5, -3, -20]",
"expected_output": "-20",
"is_hidden": True
},
{
"input_data": "[100, 200, 50, 25]",
"expected_output": "25",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Sprawdź parzystość''',
            'description': '''Napisz funkcję, która sprawdza czy liczba jest parzysta.

**Przykład:**
```
Input: 4
Output: True

Input: 7
Output: False
```

**Ograniczenia:**
- Liczba jest całkowita''',
            'difficulty': '''easy''',
            'points': 10,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_even(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_even(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_even(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isEven(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "4",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "7",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "-2",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Policz samogłoski''',
            'description': '''Napisz funkcję, która zlicza samogłoski (a, e, i, o, u) w ciągu znaków.

**Przykład:**
```
Input: "hello world"
Output: 3
```

**Ograniczenia:**
- Ignoruj wielkość liter
- Polskie znaki nie są brane pod uwagę''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_vowels(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function count_vowels(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Count_vowels(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countVowels(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello world",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "AEIOU",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "xyz",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "Programming",
"expected_output": "3",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Druga największa liczba''',
            'description': '''Znajdź drugą największą liczbę w tablicy. Jeśli nie istnieje, zwróć -1.

**Przykład:**
```
Input: [3, 1, 4, 1, 5, 9, 2, 6]
Output: 6
```

**Ograniczenia:**
- Tablica może mieć duplikaty
- Zwróć -1 jeśli nie ma drugiej największej liczby''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def second_largest(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function second_largest(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Second_largest(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> secondLargest(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3, 1, 4, 1, 5, 9, 2, 6]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[5, 5, 5]",
"expected_output": "-1",
"is_hidden": False
},
{
"input_data": "[10, 20]",
"expected_output": "10",
"is_hidden": True
},
{
"input_data": "[1]",
"expected_output": "-1",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Usuń duplikaty''',
            'description': '''Usuń duplikaty z tablicy zachowując kolejność pierwszego wystąpienia.

**Przykład:**
```
Input: [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]
```

**Ograniczenia:**
- Zachowaj kolejność elementów''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def remove_duplicates(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function remove_duplicates(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static List<int> Remove_duplicates(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> removeDuplicates(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 2, 3, 4, 4, 5]",
"expected_output": "[1, 2, 3, 4, 5]",
"is_hidden": False
},
{
"input_data": "[1, 1, 1]",
"expected_output": "[1]",
"is_hidden": False
},
{
"input_data": "[1, 2, 3]",
"expected_output": "[1, 2, 3]",
"is_hidden": True
},
{
"input_data": "[]",
"expected_output": "[]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Silnia''',
            'description': '''Oblicz silnię liczby n (n!).

**Przykład:**
```
Input: 5
Output: 120  (5! = 5 × 4 × 3 × 2 × 1)
```

**Ograniczenia:**
- 0 ≤ n ≤ 20
- 0! = 1''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def factorial(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function factorial(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static long Factorial(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto factorial(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "5",
"expected_output": "120",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "10",
"expected_output": "3628800",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Potęgowanie''',
            'description': '''Oblicz x do potęgi n (x^n).

**Przykład:**
```
Input: x=2, n=3
Output: 8
```

**Ograniczenia:**
- -100 ≤ x ≤ 100
- 0 ≤ n ≤ 20''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def power(x, n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function power(x, n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static long Power(int x, int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int power(int x, int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "2, 3",
"expected_output": "8",
"is_hidden": False
},
{
"input_data": "5, 0",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "2, 10",
"expected_output": "1024",
"is_hidden": True
},
{
"input_data": "-2, 3",
"expected_output": "-8",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Suma cyfr''',
            'description': '''Oblicz sumę cyfr liczby.

**Przykład:**
```
Input: 12345
Output: 15  (1 + 2 + 3 + 4 + 5)
```

**Ograniczenia:**
- Liczba może być ujemna (ignoruj znak minus)''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def sum_of_digits(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function sum_of_digits(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Sum_of_digits(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int sumOfDigits(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "12345",
"expected_output": "15",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "-123",
"expected_output": "6",
"is_hidden": True
},
{
"input_data": "9999",
"expected_output": "36",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Odwróć tablicę''',
            'description': '''Odwróć kolejność elementów w tablicy.

**Przykład:**
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

**Ograniczenia:**
- Nie używaj wbudowanych funkcji reverse''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def reverse_array(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function reverse_array(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static List<int> Reverse_array(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> reverseArray(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4, 5]",
"expected_output": "[5, 4, 3, 2, 1]",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "[1]",
"is_hidden": False
},
{
"input_data": "[]",
"expected_output": "[]",
"is_hidden": True
},
{
"input_data": "[10, 20]",
"expected_output": "[20, 10]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Najdłuższe słowo''',
            'description': '''Znajdź długość najdłuższego słowa w zdaniu.

**Przykład:**
```
Input: "The quick brown fox"
Output: 5
```

**Ograniczenia:**
- Słowa oddzielone spacjami
- Ignoruj znaki interpunkcyjne''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def longest_word_length(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longest_word_length(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Longest_word_length(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto longestWordLength(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "The quick brown fox",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "Hello",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "a bb ccc",
"expected_output": "3",
"is_hidden": True
},
{
"input_data": "I love programming",
"expected_output": "11",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Rok przestępny''',
            'description': '''Sprawdź czy rok jest przestępny.

Rok przestępny:
- Podzielny przez 4 ORAZ
- Niepodzielny przez 100 LUB podzielny przez 400

**Przykład:**
```
Input: 2020
Output: True

Input: 1900
Output: False
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_leap_year(year):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_leap_year(year) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_leap_year(int year) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isLeapYear(auto year) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "2020",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "1900",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "2000",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "2021",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Konwersja temperatury''',
            'description': '''Konwertuj temperaturę z Celsjusza na Fahrenheit.

Formula: F = (C × 9/5) + 32

**Przykład:**
```
Input: 0
Output: 32

Input: 100
Output: 212
```''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def celsius_to_fahrenheit(celsius):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function celsius_to_fahrenheit(celsius) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Celsius_to_fahrenheit(int celsius) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto celsiusToFahrenheit(auto celsius) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "0",
"expected_output": "32",
"is_hidden": False
},
{
"input_data": "100",
"expected_output": "212",
"is_hidden": False
},
{
"input_data": "-40",
"expected_output": "-40",
"is_hidden": True
},
{
"input_data": "20",
"expected_output": "68",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''NWW - Najmniejsza wspólna wielokrotność''',
            'description': '''Znajdź najmniejszą wspólną wielokrotność (NWW) dwóch liczb.

**Przykład:**
```
Input: a=12, b=18
Output: 36
```

**Wskazówka:**
NWW(a, b) = (a × b) / NWD(a, b)

**Ograniczenia:**
- 1 ≤ a, b ≤ 1000''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def lcm(a, b):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function lcm(a, b) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Lcm(int a, int b) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto lcm(auto a, auto b) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "12, 18",
"expected_output": "36",
"is_hidden": False
},
{
"input_data": "5, 7",
"expected_output": "35",
"is_hidden": False
},
{
"input_data": "10, 10",
"expected_output": "10",
"is_hidden": True
},
{
"input_data": "3, 5",
"expected_output": "15",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Znajdź dzielniki''',
            'description': '''Znajdź wszystkie dzielniki liczby i zwróć ich liczbę.

**Przykład:**
```
Input: 12
Output: 6  (dzielniki: 1, 2, 3, 4, 6, 12)
```

**Ograniczenia:**
- n > 0''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_divisors(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function count_divisors(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Count_divisors(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countDivisors(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "12",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "7",
"expected_output": "2",
"is_hidden": True
},
{
"input_data": "20",
"expected_output": "6",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Anagram''',
            'description': '''Sprawdź czy dwa ciągi są anagramami (zawierają te same litery).

**Przykład:**
```
Input: s1="listen", s2="silent"
Output: True

Input: s1="hello", s2="world"
Output: False
```

**Ograniczenia:**
- Ignoruj wielkość liter
- Ignoruj spacje''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_anagram(s1, s2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_anagram(s1, s2) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_anagram(str s1, str s2) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isAnagram(const string& s1, const string& s2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "listen, silent",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "hello, world",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "The eyes, They see",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "a, b",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Zlicz wystąpienia''',
            'description': '''Zlicz ile razy znak występuje w ciągu.

**Przykład:**
```
Input: s="hello", c='l'
Output: 2
```

**Ograniczenia:**
- Rozróżniaj wielkość liter''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_char(s, c):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function count_char(s, c) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Count_char(str s, str c) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countChar(const string& s, auto c) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello, l",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "programming, m",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "test, x",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "aaa, a",
"expected_output": "3",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Średnia z tablicy''',
            'description': '''Oblicz średnią arytmetyczną liczb w tablicy (zaokrąglij w dół).

**Przykład:**
```
Input: [1, 2, 3, 4, 5]
Output: 3
```

**Ograniczenia:**
- Tablica nie jest pusta
- Zwróć liczbę całkowitą (zaokrąglenie w dół)''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def average(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function average(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Average(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> average(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4, 5]",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[10]",
"expected_output": "10",
"is_hidden": False
},
{
"input_data": "[2, 4, 6, 8]",
"expected_output": "5",
"is_hidden": True
},
{
"input_data": "[1, 1, 1, 1]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Liczba Armstrong''',
            'description': '''Sprawdź czy liczba jest liczbą Armstronga.

Liczba Armstronga: suma cyfr podniesionych do potęgi równej liczbie cyfr.

**Przykład:**
```
Input: 153
Output: True  (1³ + 5³ + 3³ = 1 + 125 + 27 = 153)

Input: 123
Output: False
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_armstrong(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_armstrong(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_armstrong(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isArmstrong(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "153",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "9",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "123",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "9474",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Maksymalny iloczyn dwóch liczb''',
            'description': '''Znajdź maksymalny iloczyn dwóch różnych elementów w tablicy.

**Przykład:**
```
Input: [1, 5, 2, 8, 3]
Output: 40  (5 × 8)
```

**Ograniczenia:**
- Tablica ma co najmniej 2 elementy
- Liczby mogą być ujemne''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_product(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function max_product(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Max_product(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxProduct(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 5, 2, 8, 3]",
"expected_output": "40",
"is_hidden": False
},
{
"input_data": "[-10, -5, 1, 2]",
"expected_output": "50",
"is_hidden": False
},
{
"input_data": "[2, 3]",
"expected_output": "6",
"is_hidden": True
},
{
"input_data": "[0, 0, 0]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Kapitalizuj wyrazy''',
            'description': '''Zamień pierwszą literę każdego słowa na wielką.

**Przykład:**
```
Input: "hello world"
Output: "Hello World"
```

**Ograniczenia:**
- Słowa oddzielone spacjami
- Pozostałe litery pozostają bez zmian''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def capitalize_words(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function capitalize_words(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static string Capitalize_words(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto capitalizeWords(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello world",
"expected_output": "Hello World",
"is_hidden": False
},
{
"input_data": "a",
"expected_output": "A",
"is_hidden": False
},
{
"input_data": "the quick brown fox",
"expected_output": "The Quick Brown Fox",
"is_hidden": True
},
{
"input_data": "i love code",
"expected_output": "I Love Code",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Suma elementów tablicy''',
            'description': '''Oblicz sumę wszystkich elementów w tablicy.

**Przykład:**
```
Input: [1, 2, 3, 4, 5]
Output: 15
```''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def array_sum(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function array_sum(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Array_sum(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> arraySum(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4, 5]",
"expected_output": "15",
"is_hidden": False
},
{
"input_data": "[10]",
"expected_output": "10",
"is_hidden": False
},
{
"input_data": "[-5, 5]",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[0, 0, 0]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Znajdź indeks elementu''',
            'description': '''Znajdź indeks pierwszego wystąpienia elementu w tablicy. Zwróć -1 jeśli nie znaleziono.

**Przykład:**
```
Input: arr=[1, 2, 3, 4, 5], target=3
Output: 2
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_index(arr, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function find_index(arr, target) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Find_index(list arr, int target) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findIndex(const vector<int>& arr, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4, 5], 3",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[10, 20, 30], 20",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[5, 5, 5], 5",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[1, 2, 3], 10",
"expected_output": "-1",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Posortowana tablica''',
            'description': '''Sprawdź czy tablica jest posortowana rosnąco.

**Przykład:**
```
Input: [1, 2, 3, 4, 5]
Output: True

Input: [1, 3, 2]
Output: False
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_sorted(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_sorted(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_sorted(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isSorted(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4, 5]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "[1, 3, 2]",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "[5]",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "[1, 1, 1]",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Rotacja tablicy w lewo''',
            'description': '''Przesuń elementy tablicy o k pozycji w lewo.

**Przykład:**
```
Input: arr=[1, 2, 3, 4, 5], k=2
Output: [3, 4, 5, 1, 2]
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def rotate_left(arr, k):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function rotate_left(arr, k) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static List<int> Rotate_left(list arr, int k) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto rotateLeft(const vector<int>& arr, int k) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4, 5], 2",
"expected_output": "[3, 4, 5, 1, 2]",
"is_hidden": False
},
{
"input_data": "[1, 2], 1",
"expected_output": "[2, 1]",
"is_hidden": False
},
{
"input_data": "[1, 2, 3], 0",
"expected_output": "[1, 2, 3]",
"is_hidden": True
},
{
"input_data": "[5], 10",
"expected_output": "[5]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Parzyste i nieparzyste''',
            'description': '''Policz ile jest liczb parzystych i nieparzystych w tablicy. Zwróć różnicę (parzyste - nieparzyste).

**Przykład:**
```
Input: [1, 2, 3, 4, 5, 6]
Output: 0  (3 parzyste - 3 nieparzyste)
```''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def even_odd_diff(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function even_odd_diff(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Even_odd_diff(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> evenOddDiff(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4, 5, 6]",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "[2, 4, 6]",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[1, 3, 5]",
"expected_output": "-3",
"is_hidden": True
},
{
"input_data": "[10]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Iloczyn tablicy''',
            'description': '''Oblicz iloczyn wszystkich elementów tablicy.

**Przykład:**
```
Input: [1, 2, 3, 4]
Output: 24
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def array_product(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function array_product(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static long Array_product(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> arrayProduct(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4]",
"expected_output": "24",
"is_hidden": False
},
{
"input_data": "[5]",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "[2, 0, 5]",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[1, 1, 1]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Elementy większe od sąsiadów''',
            'description': '''Znajdź wszystkie elementy większe od obu sąsiadów. Zwróć ich liczbę.

**Przykład:**
```
Input: [1, 3, 2, 4, 1]
Output: 2  (3 i 4 są większe od swoich sąsiadów)
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def peaks_count(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function peaks_count(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Peaks_count(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> peaksCount(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 3, 2, 4, 1]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1, 2, 3]",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "[5, 1, 5]",
"expected_output": "2",
"is_hidden": True
},
{
"input_data": "[1, 1, 1]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Połącz posortowane tablice''',
            'description': '''Połącz dwie posortowane tablice w jedną posortowaną.

**Przykład:**
```
Input: arr1=[1, 3, 5], arr2=[2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def merge_sorted(arr1, arr2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function merge_sorted(arr1, arr2) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static List<int> Merge_sorted(list arr1, list arr2) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto mergeSorted(auto arr1, auto arr2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 3, 5], [2, 4, 6]",
"expected_output": "[1, 2, 3, 4, 5, 6]",
"is_hidden": False
},
{
"input_data": "[1], [2]",
"expected_output": "[1, 2]",
"is_hidden": False
},
{
"input_data": "[], [1, 2, 3]",
"expected_output": "[1, 2, 3]",
"is_hidden": True
},
{
"input_data": "[1, 2, 3], []",
"expected_output": "[1, 2, 3]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Missing Number''',
            'description': '''Tablica zawiera liczby od 0 do n z jedną brakującą. Znajdź brakującą liczbę.

**Przykład:**
```
Input: [0, 1, 3, 4]
Output: 2
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def missing_number(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function missing_number(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Missing_number(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int missingNumber(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[0, 1, 3, 4]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1, 2, 3]",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[0, 1, 2, 3, 4, 5, 7]",
"expected_output": "6",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Kadane's Algorithm''',
            'description': '''Znajdź maksymalną sumę podtablicy ciągłej (Kadane's Algorithm).

**Przykład:**
```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6  (podtablica [4, -1, 2, 1])
```''',
            'difficulty': '''hard''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_subarray(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function max_subarray(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Max_subarray(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxSubarray(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[-2, 1, -3, 4, -1, 2, 1, -5, 4]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[-1, -2, -3]",
"expected_output": "-1",
"is_hidden": True
},
{
"input_data": "[5, 4, -1, 7, 8]",
"expected_output": "23",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Unikalne elementy''',
            'description': '''Policz ile jest unikalnych elementów w tablicy.

**Przykład:**
```
Input: [1, 2, 2, 3, 3, 3]
Output: 3
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_unique(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function count_unique(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Count_unique(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countUnique(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 2, 3, 3, 3]",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[1, 1, 1]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[1, 2, 3, 4, 5]",
"expected_output": "5",
"is_hidden": True
},
{
"input_data": "[]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Move Zeros''',
            'description': '''Przenieś wszystkie zera na koniec tablicy zachowując kolejność innych elementów.

**Przykład:**
```
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def move_zeros(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function move_zeros(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static List<int> Move_zeros(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> moveZeros(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[0, 1, 0, 3, 12]",
"expected_output": "[1, 3, 12, 0, 0]",
"is_hidden": False
},
{
"input_data": "[0, 0, 1]",
"expected_output": "[1, 0, 0]",
"is_hidden": False
},
{
"input_data": "[1, 2, 3]",
"expected_output": "[1, 2, 3]",
"is_hidden": True
},
{
"input_data": "[0]",
"expected_output": "[0]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Suma pary''',
            'description': '''Sprawdź czy istnieje para liczb, której suma równa się targetowi.

**Przykład:**
```
Input: arr=[1, 2, 3, 4, 5], target=9
Output: True  (4 + 5 = 9)
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def has_pair_sum(arr, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function has_pair_sum(arr, target) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Has_pair_sum(list arr, int target) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool hasPairSum(const vector<int>& arr, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3, 4, 5], 9",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "[1, 2, 3], 10",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "[5, 5], 10",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "[1], 1",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Liczba inwersji''',
            'description': '''Policz liczbę inwersji w tablicy. Inwersja to para (i, j) gdzie i < j oraz arr[i] > arr[j].

**Przykład:**
```
Input: [2, 4, 1, 3, 5]
Output: 3  (pary: (2,1), (4,1), (4,3))
```''',
            'difficulty': '''hard''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_inversions(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function count_inversions(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Count_inversions(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countInversions(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2, 4, 1, 3, 5]",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[1, 2, 3]",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "[3, 2, 1]",
"expected_output": "3",
"is_hidden": True
},
{
"input_data": "[1]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Najdłuższy ciąg kolejnych''',
            'description': '''Znajdź długość najdłuższego ciągu kolejnych liczb.

**Przykład:**
```
Input: [100, 4, 200, 1, 3, 2]
Output: 4  (ciąg 1, 2, 3, 4)
```''',
            'difficulty': '''hard''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def longest_consecutive(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longest_consecutive(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Longest_consecutive(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int longestConsecutive(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[100, 4, 200, 1, 3, 2]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[1, 2, 0, 1]",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[9, 1, 4, 7, 3, 2, 8, 5, 6]",
"expected_output": "9",
"is_hidden": True
},
{
"input_data": "[]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Długość stringa''',
            'description': '''Zwróć długość ciągu znaków.

**Przykład:**
```
Input: "hello"
Output: 5
```''',
            'difficulty': '''easy''',
            'points': 10,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def string_length(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function string_length(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int String_length(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto stringLength(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "a",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "Hello World",
"expected_output": "11",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Pierwsza litera wielka''',
            'description': '''Zmień pierwszą literę na wielką.

**Przykład:**
```
Input: "hello"
Output: "Hello"
```''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def capitalize_first(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function capitalize_first(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static string Capitalize_first(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto capitalizeFirst(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello",
"expected_output": "Hello",
"is_hidden": False
},
{
"input_data": "world",
"expected_output": "World",
"is_hidden": False
},
{
"input_data": "A",
"expected_output": "A",
"is_hidden": True
},
{
"input_data": "",
"expected_output": "",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Usuń spacje''',
            'description': '''Usuń wszystkie spacje z ciągu.

**Przykład:**
```
Input: "hello world"
Output: "helloworld"
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def remove_spaces(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function remove_spaces(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static string Remove_spaces(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto removeSpaces(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello world",
"expected_output": "helloworld",
"is_hidden": False
},
{
"input_data": "a b c",
"expected_output": "abc",
"is_hidden": False
},
{
"input_data": "test",
"expected_output": "test",
"is_hidden": True
},
{
"input_data": "   ",
"expected_output": "",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Podciąg''',
            'description': '''Sprawdź czy s2 jest podciągiem s1.

**Przykład:**
```
Input: s1="hello", s2="ell"
Output: True
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_substring(s1, s2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_substring(s1, s2) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_substring(str s1, str s2) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isSubstring(const string& s1, const string& s2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello, ell",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "world, or",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "test, abc",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "a, a",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Odwróć słowa''',
            'description': '''Odwróć kolejność słów w zdaniu.

**Przykład:**
```
Input: "hello world"
Output: "world hello"
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def reverse_words(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function reverse_words(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static string Reverse_words(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto reverseWords(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello world",
"expected_output": "world hello",
"is_hidden": False
},
{
"input_data": "a b c",
"expected_output": "c b a",
"is_hidden": False
},
{
"input_data": "test",
"expected_output": "test",
"is_hidden": True
},
{
"input_data": "one two three",
"expected_output": "three two one",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Usuń duplikaty z ciągu''',
            'description': '''Usuń powtarzające się znaki z ciągu (zachowaj pierwsze wystąpienie).

**Przykład:**
```
Input: "hello"
Output: "helo"
```''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def remove_duplicate_chars(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function remove_duplicate_chars(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static string Remove_duplicate_chars(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto removeDuplicateChars(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello",
"expected_output": "helo",
"is_hidden": False
},
{
"input_data": "aaa",
"expected_output": "a",
"is_hidden": False
},
{
"input_data": "abc",
"expected_output": "abc",
"is_hidden": True
},
{
"input_data": "",
"expected_output": "",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Most Frequent Character''',
            'description': '''Znajdź najczęściej występujący znak w ciągu. Jeśli jest remis, zwróć pierwszy alfabetycznie.

**Przykład:**
```
Input: "hello"
Output: "l"
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def most_frequent_char(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function most_frequent_char(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static string Most_frequent_char(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto mostFrequentChar(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello",
"expected_output": "l",
"is_hidden": False
},
{
"input_data": "aabbcc",
"expected_output": "a",
"is_hidden": False
},
{
"input_data": "programming",
"expected_output": "g",
"is_hidden": True
},
{
"input_data": "a",
"expected_output": "a",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Poprawne nawiasy''',
            'description': '''Sprawdź czy nawiasy są poprawnie sparowane. Obsługuj: (), [], {}

**Przykład:**
```
Input: "()[]{}"
Output: True

Input: "(]"
Output: False
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def valid_parentheses(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function valid_parentheses(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Valid_parentheses(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool validParentheses(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "()[]{}",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "(]",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "([)]",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "{[()]}",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Longest Palindrome Substring''',
            'description': '''Znajdź długość najdłuższego palindromu w ciągu.

**Przykład:**
```
Input: "babad"
Output: 3  ("bab" lub "aba")
```''',
            'difficulty': '''hard''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def longest_palindrome_length(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longest_palindrome_length(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Longest_palindrome_length(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto longestPalindromeLength(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "babad",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "cbbd",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "a",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "racecar",
"expected_output": "7",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Pierwsza niepowtarzająca się''',
            'description': '''Znajdź pierwszy niepowtarzający się znak. Zwróć jego indeks lub -1.

**Przykład:**
```
Input: "leetcode"
Output: 0  ('l' na pozycji 0)
```''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def first_unique_char(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function first_unique_char(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int First_unique_char(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto firstUniqueChar(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "leetcode",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "loveleetcode",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "aabb",
"expected_output": "-1",
"is_hidden": True
},
{
"input_data": "z",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Kompresja ciągu''',
            'description': '''Skompresuj ciąg używając liczby powtórzeń. Jeśli skompresowany jest dłuższy, zwróć oryginalny.

**Przykład:**
```
Input: "aabcccccaaa"
Output: "a2b1c5a3"
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def compress_string(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function compress_string(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static string Compress_string(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

string compressString(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "aabcccccaaa",
"expected_output": "a2b1c5a3",
"is_hidden": False
},
{
"input_data": "abc",
"expected_output": "abc",
"is_hidden": False
},
{
"input_data": "aaa",
"expected_output": "a3",
"is_hidden": True
},
{
"input_data": "a",
"expected_output": "a",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Rotacja ciągu''',
            'description': '''Sprawdź czy s2 jest rotacją s1.

**Przykład:**
```
Input: s1="waterbottle", s2="erbottlewat"
Output: True
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_rotation(s1, s2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_rotation(s1, s2) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_rotation(str s1, str s2) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isRotation(const string& s1, const string& s2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "waterbottle, erbottlewat",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "hello, lohel",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "abc, bcd",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "aa, aa",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Zlicz słowa''',
            'description': '''Policz liczbę słów w zdaniu (słowa oddzielone spacjami).

**Przykład:**
```
Input: "hello world"
Output: 2
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_words(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function count_words(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Count_words(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countWords(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello world",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "a b c",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "test",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Toggle Case''',
            'description': '''Zamień małe litery na wielkie i odwrotnie.

**Przykład:**
```
Input: "HeLLo"
Output: "hEllO"
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def toggle_case(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function toggle_case(s) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static string Toggle_case(str s) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto toggleCase(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "HeLLo",
"expected_output": "hEllO",
"is_hidden": False
},
{
"input_data": "ABC",
"expected_output": "abc",
"is_hidden": False
},
{
"input_data": "xyz",
"expected_output": "XYZ",
"is_hidden": True
},
{
"input_data": "123",
"expected_output": "123",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Longest Common Prefix''',
            'description': '''Znajdź najdłuższy wspólny prefiks tablicy stringów. Zwróć jego długość.

**Przykład:**
```
Input: ["flower", "flow", "flight"]
Output: 2  ("fl")
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def longest_common_prefix_len(strs):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longest_common_prefix_len(strs) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Longest_common_prefix_len(list strs) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> longestCommonPrefixLen(const vector<string>& strs) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[\"flower\", \"flow\", \"flight\"]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[\"dog\", \"racecar\", \"car\"]",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "[\"test\", \"test\"]",
"expected_output": "4",
"is_hidden": True
},
{
"input_data": "[\"a\"]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Liczba doskonała''',
            'description': '''Sprawdź czy liczba jest liczbą doskonałą (równa sumie swoich dzielników).

**Przykład:**
```
Input: 6
Output: True  (6 = 1 + 2 + 3)

Input: 28
Output: True  (28 = 1 + 2 + 4 + 7 + 14)
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_perfect(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_perfect(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_perfect(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isPerfect(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "6",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "28",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "12",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "1",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Prime Factors''',
            'description': '''Zwróć liczbę różnych czynników pierwszych liczby.

**Przykład:**
```
Input: 12
Output: 2  (czynniki: 2, 3)
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_prime_factors(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function count_prime_factors(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Count_prime_factors(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countPrimeFactors(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "12",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "30",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "7",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "1",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Collatz Conjecture''',
            'description': '''Ile kroków zajmuje osiągnięcie 1 w sekwencji Collatza? (jeśli parzyste /2, jeśli nieparzyste *3+1)

**Przykład:**
```
Input: 6
Output: 8  (6→3→10→5→16→8→4→2→1)
```''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def collatz_steps(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function collatz_steps(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Collatz_steps(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto collatzSteps(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "6",
"expected_output": "8",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "3",
"expected_output": "7",
"is_hidden": True
},
{
"input_data": "10",
"expected_output": "6",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Suma kwadratów''',
            'description': '''Oblicz sumę kwadratów liczb od 1 do n.

**Przykład:**
```
Input: 3
Output: 14  (1² + 2² + 3² = 1 + 4 + 9)
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def sum_of_squares(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function sum_of_squares(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static long Sum_of_squares(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int sumOfSquares(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "3",
"expected_output": "14",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "5",
"expected_output": "55",
"is_hidden": True
},
{
"input_data": "10",
"expected_output": "385",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Binary to Decimal''',
            'description': '''Konwertuj liczbę binarną (jako string) na dziesiętną.

**Przykład:**
```
Input: "1010"
Output: 10
```''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def binary_to_decimal(binary):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function binary_to_decimal(binary) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Binary_to_decimal(str binary) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto binaryToDecimal(auto binary) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "1010",
"expected_output": "10",
"is_hidden": False
},
{
"input_data": "1111",
"expected_output": "15",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Nth Fibonacci''',
            'description': '''Zwróć n-tą liczbę Fibonacciego (0, 1, 1, 2, 3, 5, 8...).

**Przykład:**
```
Input: 6
Output: 8
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def nth_fibonacci(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function nth_fibonacci(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static long Nth_fibonacci(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto nthFibonacci(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "6",
"expected_output": "8",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "10",
"expected_output": "55",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Reverse Integer''',
            'description': '''Odwróć cyfry liczby całkowitej.

**Przykład:**
```
Input: 123
Output: 321

Input: -123
Output: -321
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def reverse_integer(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function reverse_integer(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Reverse_integer(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int reverseInteger(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "123",
"expected_output": "321",
"is_hidden": False
},
{
"input_data": "-123",
"expected_output": "-321",
"is_hidden": False
},
{
"input_data": "120",
"expected_output": "21",
"is_hidden": True
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Power of Two''',
            'description': '''Sprawdź czy liczba jest potęgą dwójki.

**Przykład:**
```
Input: 16
Output: True

Input: 18
Output: False
```''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_power_of_two(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_power_of_two(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_power_of_two(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isPowerOfTwo(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "16",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "18",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "0",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Happy Number''',
            'description': '''Sprawdź czy liczba jest "happy number". Proces: zamień na sumę kwadratów cyfr. Powtarzaj. Jeśli osiągniesz 1, to happy number.

**Przykład:**
```
Input: 19
Output: True  (19→82→68→100→1)
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_happy(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function is_happy(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Is_happy(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isHappy(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "19",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "2",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "7",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Trailing Zeros Factorial''',
            'description': '''Policz ile zer końcowych ma silnia n!

**Przykład:**
```
Input: 5
Output: 1  (5! = 120)

Input: 10
Output: 2  (10! = 3628800)
```''',
            'difficulty': '''hard''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def trailing_zeros(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function trailing_zeros(n) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Trailing_zeros(int n) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto trailingZeros(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "5",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "10",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "25",
"expected_output": "6",
"is_hidden": True
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Wyszukiwanie liniowe''',
            'description': '''Wyszukaj element w tablicy metodą liniową. Zwróć indeks lub -1.

**Przykład:**
```
Input: arr=[5, 3, 7, 1], target=7
Output: 2
```''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def linear_search(arr, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function linear_search(arr, target) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Linear_search(list arr, int target) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto linearSearch(const vector<int>& arr, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[5, 3, 7, 1], 7",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1, 2, 3], 4",
"expected_output": "-1",
"is_hidden": False
},
{
"input_data": "[10], 10",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[5, 5, 5], 5",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Wyszukiwanie binarne''',
            'description': '''Wyszukaj element w posortowanej tablicy metodą binarną. Zwróć indeks lub -1.

**Przykład:**
```
Input: arr=[1, 3, 5, 7, 9], target=5
Output: 2
```''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def binary_search(arr, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function binary_search(arr, target) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Binary_search(list arr, int target) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto binarySearch(const vector<int>& arr, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 3, 5, 7, 9], 5",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1, 2, 3, 4, 5], 6",
"expected_output": "-1",
"is_hidden": False
},
{
"input_data": "[10], 10",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[1, 3, 5], 3",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Kroki sortowania przez wybieranie''',
            'description': '''Zwróć ile zamian wykonuje selection sort na tablicy.

**Przykład:**
```
Input: [3, 2, 1]
Output: 2
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def selection_sort_swaps(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function selection_sort_swaps(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Selection_sort_swaps(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> selectionSortSwaps(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3, 2, 1]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1, 2, 3]",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "[2, 1]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[5, 4, 3, 2, 1]",
"expected_output": "2",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Kroki sortowania przez wstawianie''',
            'description': '''Zwróć ile przesunięć wykonuje insertion sort.

**Przykład:**
```
Input: [3, 2, 1]
Output: 3
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def insertion_sort_shifts(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function insertion_sort_shifts(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Insertion_sort_shifts(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> insertionSortShifts(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3, 2, 1]",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[1, 2, 3]",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "[2, 1]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[4, 3, 2, 1]",
"expected_output": "6",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Quick Select''',
            'description': '''Znajdź k-ty najmniejszy element (1-indexed).

**Przykład:**
```
Input: arr=[3, 2, 1, 5, 4], k=2
Output: 2
```''',
            'difficulty': '''hard''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def kth_smallest(arr, k):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function kth_smallest(arr, k) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Kth_smallest(list arr, int k) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto kthSmallest(const vector<int>& arr, int k) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3, 2, 1, 5, 4], 2",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1], 1",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[5, 3, 1, 4, 2], 3",
"expected_output": "3",
"is_hidden": True
},
{
"input_data": "[10, 20, 30], 1",
"expected_output": "10",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Dutch National Flag''',
            'description': '''Posortuj tablicę zawierającą tylko 0, 1, 2 w czasie O(n).

**Przykład:**
```
Input: [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```''',
            'difficulty': '''hard''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def sort_colors(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function sort_colors(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static List<int> Sort_colors(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

void sortColors(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2, 0, 2, 1, 1, 0]",
"expected_output": "[0, 0, 1, 1, 2, 2]",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "[0]",
"is_hidden": False
},
{
"input_data": "[1, 2, 0]",
"expected_output": "[0, 1, 2]",
"is_hidden": True
},
{
"input_data": "[2, 2, 1, 0, 0]",
"expected_output": "[0, 0, 1, 2, 2]",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Następna permutacja''',
            'description': '''Znajdź następną permutację leksykograficzną. Jeśli nie istnieje, zwróć najmniejszą.

**Przykład:**
```
Input: [1, 2, 3]
Output: [1, 3, 2]

Input: [3, 2, 1]
Output: [1, 2, 3]
```''',
            'difficulty': '''hard''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def next_permutation(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function next_permutation(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static List<int> Next_permutation(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> nextPermutation(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1, 2, 3]",
"expected_output": "[1, 3, 2]",
"is_hidden": False
},
{
"input_data": "[3, 2, 1]",
"expected_output": "[1, 2, 3]",
"is_hidden": False
},
{
"input_data": "[1, 1, 5]",
"expected_output": "[1, 5, 1]",
"is_hidden": True
},
{
"input_data": "[1]",
"expected_output": "[1]",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Majority Element''',
            'description': '''Znajdź element występujący więcej niż n/2 razy (Boyer-Moore).

**Przykład:**
```
Input: [3, 2, 3]
Output: 3
```''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def majority_element(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function majority_element(arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Majority_element(list arr) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> majorityElement(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3, 2, 3]",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[2, 2, 1, 1, 1, 2, 2]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[1, 1, 2, 2, 1]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Trapping Rain Water''',
            'description': '''Oblicz ile wody można złapać między słupkami.

**Przykład:**
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def trap_water(heights):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function trap_water(heights) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static int Trap_water(list heights) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> trapWater(const vector<int>& heights) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[0,1,0,2,1,0,1,3,2,1,2,1]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[4,2,0,3,2,5]",
"expected_output": "9",
"is_hidden": False
},
{
"input_data": "[1,1,1]",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[3,0,2,0,4]",
"expected_output": "7",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Jump Game''',
            'description': '''Sprawdź czy możesz skoczyć z początku do końca tablicy. Każda wartość to maksymalny skok.

**Przykład:**
```
Input: [2,3,1,1,4]
Output: True

Input: [3,2,1,0,4]
Output: False
```''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def can_jump(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function can_jump(nums) {
    // Twój kod tutaj
    
}''',
            'function_signature_csharp': '''public static bool Can_jump(list nums) {
    // Twój kod tutaj
    
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool canJump(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2,3,1,1,4]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "[3,2,1,0,4]",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "[1,1,1,1]",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Konwersja Binarna na Dziesiętną''',
            'description': '''Napisz funkcję, która konwertuje liczbę binarną (jako string) na liczbę dziesiętną.

Przykład:
- Wejście: "1010"
- Wyjście: 10

- Wejście: "11111111"
- Wyjście: 255''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def binary_to_decimal(binary_str):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function binaryToDecimal(binaryStr) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int BinaryToDecimal(string binaryStr) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto binaryToDecimal(auto binary_str) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "1010",
"expected_output": "10",
"is_hidden": False
},
{
"input_data": "11111111",
"expected_output": "255",
"is_hidden": False
},
{
"input_data": "10000000",
"expected_output": "128",
"is_hidden": True
},
{
"input_data": "101010",
"expected_output": "42",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Znajdź Brakującą Liczbę''',
            'description': '''Dana jest tablica zawierająca n różnych liczb z zakresu [0, n]. Jedna liczba z tego zakresu brakuje. Znajdź ją.

Przykład:
- Wejście: [3,0,1]
- Wyjście: 2

- Wejście: [0,1]
- Wyjście: 2''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_missing_number(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function findMissingNumber(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int FindMissingNumber(int[] nums) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findMissingNumber(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3,0,1]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[0,1]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[9,6,4,2,3,5,7,0,1]",
"expected_output": "8",
"is_hidden": True
},
{
"input_data": "[0]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Obróć Tablicę''',
            'description': '''Obróć tablicę w prawo o k pozycji.

Przykład:
- Wejście: nums = [1,2,3,4,5,6,7], k = 3
- Wyjście: [5,6,7,1,2,3,4]

- Wejście: nums = [-1,-100,3,99], k = 2
- Wyjście: [3,99,-1,-100]''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def rotate_array(nums, k):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function rotateArray(nums, k) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[] RotateArray(int[] nums, int k) {
        // Twój kod tutaj
        return nums;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

void rotateArray(const vector<int>& nums, int k) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3,4,5,6,7],3",
"expected_output": "[5,6,7,1,2,3,4]",
"is_hidden": False
},
{
"input_data": "[-1,-100,3,99],2",
"expected_output": "[3,99,-1,-100]",
"is_hidden": False
},
{
"input_data": "[1,2],3",
"expected_output": "[2,1]",
"is_hidden": True
},
{
"input_data": "[1,2,3,4,5],0",
"expected_output": "[1,2,3,4,5]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Sprawdź Poprawność Nawiasów''',
            'description': '''Sprawdź czy string zawiera poprawnie zagnieżdżone nawiasy: (), [], {}.

Przykład:
- Wejście: "()"
- Wyjście: true

- Wejście: "()[]{}"
- Wyjście: true

- Wejście: "(]"
- Wyjście: false''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_valid_parentheses(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isValidParentheses(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsValidParentheses(string s) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isValidParentheses(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "()",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "()[]{}",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "(]",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "{[()]}",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Znajdź Unikalną Liczbę''',
            'description': '''W tablicy każda liczba występuje dwa razy, oprócz jednej. Znajdź tę unikalną liczbę.

Przykład:
- Wejście: [2,2,1]
- Wyjście: 1

- Wejście: [4,1,2,1,2]
- Wyjście: 4''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def single_number(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function singleNumber(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int SingleNumber(int[] nums) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> singleNumber(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2,2,1]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[4,1,2,1,2]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[7,3,5,3,5]",
"expected_output": "7",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Wspinanie po Schodach''',
            'description': '''Wspiasz się po schodach. Potrzebujesz n kroków aby dotrzeć na górę. Za każdym razem możesz wejść o 1 lub 2 stopnie. Na ile sposobów możesz dotrzeć na górę?

Przykład:
- Wejście: 2
- Wyjście: 2 (1+1 lub 2)

- Wejście: 3
- Wyjście: 3 (1+1+1, 1+2, 2+1)''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def climb_stairs(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function climbStairs(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int ClimbStairs(int n) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int climbStairs(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "2",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "3",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "5",
"expected_output": "8",
"is_hidden": True
},
{
"input_data": "10",
"expected_output": "89",
"is_hidden": True
}
],
            'tags': [],
        },
        {
            'title': '''Trójkąt Pascala''',
            'description': '''Wygeneruj pierwsze numRows wierszy trójkąta Pascala.

Przykład:
- Wejście: 5
- Wyjście: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def generate_pascal_triangle(numRows):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function generatePascalTriangle(numRows) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[][] GeneratePascalTriangle(int numRows) {
        // Twój kod tutaj
        return new int[0][];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> generatePascalTriangle(auto numRows) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "5",
"expected_output": "[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "[[1]]",
"is_hidden": False
},
{
"input_data": "3",
"expected_output": "[[1],[1,1],[1,2,1]]",
"is_hidden": True
},
{
"input_data": "6",
"expected_output": "[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Potęga Dwójki''',
            'description': '''Sprawdź czy liczba jest potęgą dwójki.

Przykład:
- Wejście: 16
- Wyjście: true

- Wejście: 3
- Wyjście: false''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_power_of_two(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isPowerOfTwo(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsPowerOfTwo(int n) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isPowerOfTwo(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "16",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "3",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "256",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Zawiera Duplikaty''',
            'description': '''Sprawdź czy tablica zawiera duplikaty.

Przykład:
- Wejście: [1,2,3,1]
- Wyjście: true

- Wejście: [1,2,3,4]
- Wyjście: false''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def contains_duplicate(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function containsDuplicate(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> containsDuplicate(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3,1]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "[1,2,3,4]",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "[1,1,1,3,3,4,3,2,4,2]",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "[]",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Przenieś Zera''',
            'description': '''Przenieś wszystkie zera na koniec tablicy zachowując kolejność pozostałych elementów.

Przykład:
- Wejście: [0,1,0,3,12]
- Wyjście: [1,3,12,0,0]''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def move_zeroes(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function moveZeroes(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[] MoveZeroes(int[] nums) {
        // Twój kod tutaj
        return nums;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> moveZeroes(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[0,1,0,3,12]",
"expected_output": "[1,3,12,0,0]",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "[0]",
"is_hidden": False
},
{
"input_data": "[1,2,3]",
"expected_output": "[1,2,3]",
"is_hidden": True
},
{
"input_data": "[0,0,1]",
"expected_output": "[1,0,0]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Część Wspólna Dwóch Tablic''',
            'description': '''Znajdź część wspólną dwóch tablic.

Przykład:
- Wejście: nums1 = [1,2,2,1], nums2 = [2,2]
- Wyjście: [2]

- Wejście: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
- Wyjście: [4,9] lub [9,4]''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def intersection(nums1, nums2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function intersection(nums1, nums2) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        // Twój kod tutaj
        return new int[0];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto intersection(auto nums1, auto nums2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,2,1],[2,2]",
"expected_output": "[2]",
"is_hidden": False
},
{
"input_data": "[4,9,5],[9,4,9,8,4]",
"expected_output": "[4,9]",
"is_hidden": False
},
{
"input_data": "[1,2,3],[4,5,6]",
"expected_output": "[]",
"is_hidden": True
},
{
"input_data": "[1],[1]",
"expected_output": "[1]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Pierwszy Unikalny Znak''',
            'description': '''Znajdź indeks pierwszego unikalnego znaku w stringu.

Przykład:
- Wejście: "leetcode"
- Wyjście: 0

- Wejście: "loveleetcode"
- Wyjście: 2

- Wejście: "aabb"
- Wyjście: -1''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def first_uniq_char(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function firstUniqChar(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int FirstUniqChar(string s) {
        // Twój kod tutaj
        return -1;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto firstUniqChar(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "leetcode",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "loveleetcode",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "aabb",
"expected_output": "-1",
"is_hidden": True
},
{
"input_data": "z",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Odwróć String''',
            'description': '''Odwróć tablicę znaków in-place.

Przykład:
- Wejście: ["h","e","l","l","o"]
- Wyjście: ["o","l","l","e","h"]

- Wejście: ["H","a","n","n","a","h"]
- Wyjście: ["h","a","n","n","a","H"]''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def reverse_string(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function reverseString(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public char[] ReverseString(char[] s) {
        // Twój kod tutaj
        return s;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto reverseString(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[\"h\",\"e\",\"l\",\"l\",\"o\"]",
"expected_output": "[\"o\",\"l\",\"l\",\"e\",\"h\"]",
"is_hidden": False
},
{
"input_data": "[\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]",
"expected_output": "[\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]",
"is_hidden": False
},
{
"input_data": "[\"A\"]",
"expected_output": "[\"A\"]",
"is_hidden": True
},
{
"input_data": "[\"a\",\"b\"]",
"expected_output": "[\"b\",\"a\"]",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Szczęśliwa Liczba''',
            'description': '''Liczba jest szczęśliwa jeśli proces zastępowania jej sumą kwadratów jej cyfr prowadzi do 1. Sprawdź czy liczba jest szczęśliwa.

Przykład:
- Wejście: 19
- Wyjście: true (1² + 9² = 82, 8² + 2² = 68, 6² + 8² = 100, 1² + 0² + 0² = 1)

- Wejście: 2
- Wyjście: false''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_happy(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isHappy(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsHappy(int n) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isHappy(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "19",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "2",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "7",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "1",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Policz Liczby Pierwsze''',
            'description': '''Policz ile jest liczb pierwszych mniejszych od n.

Przykład:
- Wejście: 10
- Wyjście: 4 (2, 3, 5, 7)

- Wejście: 0
- Wyjście: 0''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_primes(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function countPrimes(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int CountPrimes(int n) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countPrimes(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "10",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "20",
"expected_output": "8",
"is_hidden": True
},
{
"input_data": "100",
"expected_output": "25",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Czy Jest Podsekwencją''',
            'description': '''Sprawdź czy s jest podsekwencją t (czy da się uzyskać s usuwając znaki z t bez zmiany kolejności).

Przykład:
- Wejście: s = "abc", t = "ahbgdc"
- Wyjście: true

- Wejście: s = "axc", t = "ahbgdc"
- Wyjście: false''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_subsequence(s, t):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isSubsequence(s, t) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsSubsequence(string s, string t) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isSubsequence(const string& s, auto t) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "abc,ahbgdc",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "axc,ahbgdc",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "ace,abcde",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "aec,abcde",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Rzymskie na Dziesiętne''',
            'description': '''Konwertuj liczbę rzymską na dziesiętną. I=1, V=5, X=10, L=50, C=100, D=500, M=1000.

Przykład:
- Wejście: "III"
- Wyjście: 3

- Wejście: "LVIII"
- Wyjście: 58

- Wejście: "MCMXCIV"
- Wyjście: 1994''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def roman_to_int(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function romanToInt(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int RomanToInt(string s) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int romanToInt(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "III",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "LVIII",
"expected_output": "58",
"is_hidden": False
},
{
"input_data": "MCMXCIV",
"expected_output": "1994",
"is_hidden": True
},
{
"input_data": "IX",
"expected_output": "9",
"is_hidden": True
}
],
            'tags': ["strings", "math"],
        },
        {
            'title': '''Dodaj Jeden''',
            'description': '''Dana jest liczba reprezentowana jako tablica cyfr. Dodaj do niej 1.

Przykład:
- Wejście: [1,2,3]
- Wyjście: [1,2,4]

- Wejście: [9,9,9]
- Wyjście: [1,0,0,0]''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def plus_one(digits):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function plusOne(digits) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[] PlusOne(int[] digits) {
        // Twój kod tutaj
        return digits;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto plusOne(const string& digits) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3]",
"expected_output": "[1,2,4]",
"is_hidden": False
},
{
"input_data": "[9,9,9]",
"expected_output": "[1,0,0,0]",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "[1]",
"is_hidden": True
},
{
"input_data": "[9]",
"expected_output": "[1,0]",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Element większościowy''',
            'description': '''Znajdź element który występuje więcej niż ⌊n/2⌋ razy w tablicy.

Przykład:
- Wejście: [3,2,3]
- Wyjście: 3

- Wejście: [2,2,1,1,1,2,2]
- Wyjście: 2''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def majority_element(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function majorityElement(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MajorityElement(int[] nums) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> majorityElement(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3,2,3]",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[2,2,1,1,1,2,2]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[6,5,5]",
"expected_output": "5",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Numer Kolumny Excel''',
            'description': '''Konwertuj tytuł kolumny Excel na numer (A=1, B=2, ... Z=26, AA=27, AB=28, ...).

Przykład:
- Wejście: "A"
- Wyjście: 1

- Wejście: "AB"
- Wyjście: 28

- Wejście: "ZY"
- Wyjście: 701''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def title_to_number(columnTitle):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function titleToNumber(columnTitle) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int TitleToNumber(string columnTitle) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto titleToNumber(auto columnTitle) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "A",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "AB",
"expected_output": "28",
"is_hidden": False
},
{
"input_data": "ZY",
"expected_output": "701",
"is_hidden": True
},
{
"input_data": "FXSHRXW",
"expected_output": "2147483647",
"is_hidden": True
}
],
            'tags': ["strings", "math"],
        },
        {
            'title': '''Dodaj Binarne''',
            'description': '''Dodaj dwie liczby binarne (jako stringi) i zwróć wynik jako string.

Przykład:
- Wejście: a = "11", b = "1"
- Wyjście: "100"

- Wejście: a = "1010", b = "1011"
- Wyjście: "10101"''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def add_binary(a, b):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function addBinary(a, b) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public string AddBinary(string a, string b) {
        // Twój kod tutaj
        return "";
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto addBinary(auto a, auto b) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "11,1",
"expected_output": "100",
"is_hidden": False
},
{
"input_data": "1010,1011",
"expected_output": "10101",
"is_hidden": False
},
{
"input_data": "0,0",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "1111,1111",
"expected_output": "11110",
"is_hidden": True
}
],
            'tags': ["strings", "math"],
        },
        {
            'title': '''Pierwiastek Kwadratowy''',
            'description': '''Oblicz pierwiastek kwadratowy z x zaokrąglony w dół do liczby całkowitej (bez użycia wbudowanych funkcji).

Przykład:
- Wejście: 4
- Wyjście: 2

- Wejście: 8
- Wyjście: 2''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def my_sqrt(x):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function mySqrt(x) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MySqrt(int x) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto mySqrt(int x) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "4",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "8",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "16",
"expected_output": "4",
"is_hidden": True
},
{
"input_data": "1",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Sprawdź anagram''',
            'description': '''Sprawdź czy dwa stringi są anagramami (zawierają te same znaki w różnej kolejności).

Przykład:
- Wejście: s = "anagram", t = "nagaram"
- Wyjście: true

- Wejście: s = "rat", t = "car"
- Wyjście: false''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_anagram(s, t):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isAnagram(s, t) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsAnagram(string s, string t) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isAnagram(const string& s, auto t) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "anagram,nagaram",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "rat,car",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "a,a",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "ab,ba",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Długość Ostatniego Słowa''',
            'description': '''Znajdź długość ostatniego słowa w stringu. Słowo to ciąg znaków bez spacji.

Przykład:
- Wejście: "Hello World"
- Wyjście: 5

- Wejście: "   fly me   to   the moon  "
- Wyjście: 4''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def length_of_last_word(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function lengthOfLastWord(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int LengthOfLastWord(string s) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int lengthOfLastWord(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "Hello World",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "   fly me   to   the moon  ",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "a",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "a ",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Scal Posortowane Tablice''',
            'description': '''Scal dwie posortowane tablice w jedną posortowaną tablicę.

Przykład:
- Wejście: nums1 = [1,2,3], nums2 = [2,5,6]
- Wyjście: [1,2,2,3,5,6]''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def merge_sorted_arrays(nums1, nums2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function mergeSortedArrays(nums1, nums2) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[] MergeSortedArrays(int[] nums1, int[] nums2) {
        // Twój kod tutaj
        return new int[0];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto mergeSortedArrays(auto nums1, auto nums2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3],[2,5,6]",
"expected_output": "[1,2,2,3,5,6]",
"is_hidden": False
},
{
"input_data": "[1],[2]",
"expected_output": "[1,2]",
"is_hidden": False
},
{
"input_data": "[],[1]",
"expected_output": "[1]",
"is_hidden": True
},
{
"input_data": "[1,3,5],[2,4,6]",
"expected_output": "[1,2,3,4,5,6]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Usuń element''',
            'description': '''Usuń wszystkie wystąpienia wartości val z tablicy in-place. Zwróć długość nowej tablicy.

Przykład:
- Wejście: nums = [3,2,2,3], val = 3
- Wyjście: 2 (tablica: [2,2])

- Wejście: nums = [0,1,2,2,3,0,4,2], val = 2
- Wyjście: 5 (tablica: [0,1,3,0,4])''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def remove_element(nums, val):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function removeElement(nums, val) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int RemoveElement(int[] nums, int val) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto removeElement(const vector<int>& nums, auto val) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3,2,2,3],3",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[0,1,2,2,3,0,4,2],2",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "[1],1",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[4,5],4",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Zakresy Podsumowania''',
            'description': '''Zwróć najmniejszą posortowaną listę zakresów pokrywających wszystkie liczby z tablicy.

Przykład:
- Wejście: [0,1,2,4,5,7]
- Wyjście: ["0->2","4->5","7"]

- Wejście: [0,2,3,4,6,8,9]
- Wyjście: ["0","2->4","6","8->9"]''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def summary_ranges(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function summaryRanges(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public string[] SummaryRanges(int[] nums) {
        // Twój kod tutaj
        return new string[0];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> summaryRanges(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[0,1,2,4,5,7]",
"expected_output": "[\"0->2\",\"4->5\",\"7\"]",
"is_hidden": False
},
{
"input_data": "[0,2,3,4,6,8,9]",
"expected_output": "[\"0\",\"2->4\",\"6\",\"8->9\"]",
"is_hidden": False
},
{
"input_data": "[]",
"expected_output": "[]",
"is_hidden": True
},
{
"input_data": "[1]",
"expected_output": "[\"1\"]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Potęga Trójki''',
            'description': '''Sprawdź czy liczba jest potęgą trójki.

Przykład:
- Wejście: 27
- Wyjście: true

- Wejście: 0
- Wyjście: false

- Wejście: 9
- Wyjście: true''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_power_of_three(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isPowerOfThree(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsPowerOfThree(int n) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isPowerOfThree(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "27",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "9",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "45",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Odwróć Bity''',
            'description': '''Odwróć bity 32-bitowej liczby bez znaku.

Przykład:
- Wejście: 43261596 (00000010100101000001111010011100)
- Wyjście: 964176192 (00111001011110000010100101000000)''',
            'difficulty': '''easy''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def reverse_bits(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function reverseBits(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public uint ReverseBits(uint n) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto reverseBits(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "43261596",
"expected_output": "964176192",
"is_hidden": False
},
{
"input_data": "4294967293",
"expected_output": "3221225471",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "2147483648",
"is_hidden": True
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': [],
        },
        {
            'title': '''Odległość Hamminga''',
            'description': '''Oblicz odległość Hamminga między dwiema liczbami (liczba pozycji na których bity są różne).

Przykład:
- Wejście: x = 1, y = 4
- Wyjście: 2 (1 = 0001, 4 = 0100)''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def hamming_distance(x, y):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function hammingDistance(x, y) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int HammingDistance(int x, int y) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto hammingDistance(int x, int y) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "1,4",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "3,1",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "0,0",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "93,73",
"expected_output": "2",
"is_hidden": True
}
],
            'tags': [],
        },
        {
            'title': '''Znajdź element szczytowy''',
            'description': '''Znajdź indeks elementu szczytowego (większego od sąsiadów). Tablica może mieć wiele szczytów - zwróć dowolny.

Przykład:
- Wejście: [1,2,3,1]
- Wyjście: 2

- Wejście: [1,2,1,3,5,6,4]
- Wyjście: 5''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_peak_element(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function findPeakElement(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int FindPeakElement(int[] nums) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findPeakElement(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3,1]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[1,2,1,3,5,6,4]",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[1,2]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Iloczyn Bez Siebie''',
            'description': '''Zwróć tablicę gdzie answer[i] to iloczyn wszystkich elementów nums oprócz nums[i]. Bez użycia dzielenia.

Przykład:
- Wejście: [1,2,3,4]
- Wyjście: [24,12,8,6]

- Wejście: [-1,1,0,-3,3]
- Wyjście: [0,0,9,0,0]''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def product_except_self(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function productExceptSelf(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        // Twój kod tutaj
        return new int[0];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> productExceptSelf(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3,4]",
"expected_output": "[24,12,8,6]",
"is_hidden": False
},
{
"input_data": "[-1,1,0,-3,3]",
"expected_output": "[0,0,9,0,0]",
"is_hidden": False
},
{
"input_data": "[2,3,4,5]",
"expected_output": "[60,40,30,24]",
"is_hidden": True
},
{
"input_data": "[1,1]",
"expected_output": "[1,1]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Macierz Spiralna''',
            'description': '''Zwróć wszystkie elementy macierzy w kolejności spiralnej (od zewnątrz do środka).

Przykład:
- Wejście: [[1,2,3],[4,5,6],[7,8,9]]
- Wyjście: [1,2,3,6,9,8,7,4,5]''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def spiral_order(matrix):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function spiralOrder(matrix) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[] SpiralOrder(int[][] matrix) {
        // Twój kod tutaj
        return new int[0];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> spiralOrder(const vector<vector<int>>& matrix) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[1,2,3],[4,5,6],[7,8,9]]",
"expected_output": "[1,2,3,6,9,8,7,4,5]",
"is_hidden": False
},
{
"input_data": "[[1,2,3,4],[5,6,7,8],[9,10,11,12]]",
"expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]",
"is_hidden": False
},
{
"input_data": "[[1]]",
"expected_output": "[1]",
"is_hidden": True
},
{
"input_data": "[[1,2],[3,4]]",
"expected_output": "[1,2,4,3]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Obróć Obraz''',
            'description': '''Obróć macierz n×n o 90 stopni w prawo in-place.

Przykład:
- Wejście: [[1,2,3],[4,5,6],[7,8,9]]
- Wyjście: [[7,4,1],[8,5,2],[9,6,3]]''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def rotate_image(matrix):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function rotateImage(matrix) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[][] RotateImage(int[][] matrix) {
        // Twój kod tutaj
        return matrix;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> rotateImage(const vector<vector<int>>& matrix) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[1,2,3],[4,5,6],[7,8,9]]",
"expected_output": "[[7,4,1],[8,5,2],[9,6,3]]",
"is_hidden": False
},
{
"input_data": "[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]",
"expected_output": "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]",
"is_hidden": False
},
{
"input_data": "[[1]]",
"expected_output": "[[1]]",
"is_hidden": True
},
{
"input_data": "[[1,2],[3,4]]",
"expected_output": "[[3,1],[4,2]]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Ustaw Zera w Macierzy''',
            'description': '''Jeśli element macierzy wynosi 0, ustaw cały wiersz i kolumnę na 0. In-place.

Przykład:
- Wejście: [[1,1,1],[1,0,1],[1,1,1]]
- Wyjście: [[1,0,1],[0,0,0],[1,0,1]]''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def set_zeroes(matrix):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function setZeroes(matrix) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[][] SetZeroes(int[][] matrix) {
        // Twój kod tutaj
        return matrix;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> setZeroes(const vector<vector<int>>& matrix) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[1,1,1],[1,0,1],[1,1,1]]",
"expected_output": "[[1,0,1],[0,0,0],[1,0,1]]",
"is_hidden": False
},
{
"input_data": "[[0,1,2,0],[3,4,5,2],[1,3,1,5]]",
"expected_output": "[[0,0,0,0],[0,4,5,0],[0,3,1,0]]",
"is_hidden": False
},
{
"input_data": "[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]",
"expected_output": "[[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]",
"is_hidden": True
},
{
"input_data": "[[1]]",
"expected_output": "[[1]]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Szukaj w Obróconej Tablicy''',
            'description': '''Posortowana tablica została obrócona w nieznanym punkcie. Znajdź element target. O(log n).

Przykład:
- Wejście: nums = [4,5,6,7,0,1,2], target = 0
- Wyjście: 4

- Wejście: nums = [4,5,6,7,0,1,2], target = 3
- Wyjście: -1''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def search_rotated(nums, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function searchRotated(nums, target) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int SearchRotated(int[] nums, int target) {
        // Twój kod tutaj
        return -1;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int searchRotated(const vector<int>& nums, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[4,5,6,7,0,1,2],0",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[4,5,6,7,0,1,2],3",
"expected_output": "-1",
"is_hidden": False
},
{
"input_data": "[1],0",
"expected_output": "-1",
"is_hidden": True
},
{
"input_data": "[1,3],3",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Pojemnik z Najwięcej Wody''',
            'description': '''Dana jest tablica wysokości. Znajdź dwie linie, które razem z osią X tworzą pojemnik zawierający najwięcej wody.

Przykład:
- Wejście: [1,8,6,2,5,4,8,3,7]
- Wyjście: 49''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_area(height):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maxArea(height) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MaxArea(int[] height) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxArea(const vector<int>& height) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,8,6,2,5,4,8,3,7]",
"expected_output": "49",
"is_hidden": False
},
{
"input_data": "[1,1]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[4,3,2,1,4]",
"expected_output": "16",
"is_hidden": True
},
{
"input_data": "[1,2,1]",
"expected_output": "2",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Suma trójek''',
            'description': '''Znajdź wszystkie unikalne trójki w tablicy, które sumują się do 0.

Przykład:
- Wejście: [-1,0,1,2,-1,-4]
- Wyjście: [[-1,-1,2],[-1,0,1]]''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def three_sum(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function threeSum(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[][] ThreeSum(int[] nums) {
        // Twój kod tutaj
        return new int[0][];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> threeSum(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[-1,0,1,2,-1,-4]",
"expected_output": "[[-1,-1,2],[-1,0,1]]",
"is_hidden": False
},
{
"input_data": "[]",
"expected_output": "[]",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "[]",
"is_hidden": True
},
{
"input_data": "[0,0,0]",
"expected_output": "[[0,0,0]]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Najdłuższy Podciąg Bez Powtórzeń''',
            'description': '''Znajdź długość najdłuższego podciągu bez powtarzających się znaków.

Przykład:
- Wejście: "abcabcbb"
- Wyjście: 3 ("abc")

- Wejście: "bbbbb"
- Wyjście: 1 ("b")''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def length_of_longest_substring(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function lengthOfLongestSubstring(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int LengthOfLongestSubstring(string s) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int lengthOfLongestSubstring(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "abcabcbb",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "bbbbb",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "pwwkew",
"expected_output": "3",
"is_hidden": True
},
{
"input_data": "",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Gra w Skoki''',
            'description': '''Możesz skoczyć maksymalnie nums[i] kroków z pozycji i. Sprawdź czy możesz dotrzeć do ostatniego indeksu.

Przykład:
- Wejście: [2,3,1,1,4]
- Wyjście: true

- Wejście: [3,2,1,0,4]
- Wyjście: false''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def can_jump(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function canJump(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool CanJump(int[] nums) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool canJump(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2,3,1,1,4]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "[3,2,1,0,4]",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "[2,0,0]",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Wydawanie Reszty''',
            'description': '''Masz monety o różnych nominałach. Znajdź minimalną liczbę monet potrzebną do wydania amount. Zwróć -1 jeśli niemożliwe.

Przykład:
- Wejście: coins = [1,2,5], amount = 11
- Wyjście: 3 (5+5+1)

- Wejście: coins = [2], amount = 3
- Wyjście: -1''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def coin_change(coins, amount):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function coinChange(coins, amount) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int CoinChange(int[] coins, int amount) {
        // Twój kod tutaj
        return -1;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int coinChange(const vector<int>& coins, int amount) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,5],11",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[2],3",
"expected_output": "-1",
"is_hidden": False
},
{
"input_data": "[1],0",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[1,2,5],100",
"expected_output": "20",
"is_hidden": True
}
],
            'tags': [],
        },
        {
            'title': '''Najdłuższy Palindrom''',
            'description': '''Znajdź najdłuższy podciąg będący palindromem.

Przykład:
- Wejście: "babad"
- Wyjście: "bab" lub "aba"

- Wejście: "cbbd"
- Wyjście: "bb"''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def longest_palindrome(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longestPalindrome(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public string LongestPalindrome(string s) {
        // Twój kod tutaj
        return "";
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int longestPalindrome(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "babad",
"expected_output": "bab",
"is_hidden": False
},
{
"input_data": "cbbd",
"expected_output": "bb",
"is_hidden": False
},
{
"input_data": "a",
"expected_output": "a",
"is_hidden": True
},
{
"input_data": "ac",
"expected_output": "a",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Grupuj anagramy''',
            'description': '''Pogrupuj anagramy razem.

Przykład:
- Wejście: ["eat","tea","tan","ate","nat","bat"]
- Wyjście: [["bat"],["nat","tan"],["ate","eat","tea"]]''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def group_anagrams(strs):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function groupAnagrams(strs) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public string[][] GroupAnagrams(string[] strs) {
        // Twój kod tutaj
        return new string[0][];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> groupAnagrams(const vector<string>& strs) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]",
"expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]",
"is_hidden": False
},
{
"input_data": "[\"\"]",
"expected_output": "[[\"\"]]",
"is_hidden": False
},
{
"input_data": "[\"a\"]",
"expected_output": "[[\"a\"]]",
"is_hidden": True
},
{
"input_data": "[\"abc\",\"bca\",\"cab\",\"xyz\"]",
"expected_output": "[[\"abc\",\"bca\",\"cab\"],[\"xyz\"]]",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Podział Słowa''',
            'description': '''Sprawdź czy string s może być podzielony na słowa ze słownika wordDict.

Przykład:
- Wejście: s = "leetcode", wordDict = ["leet","code"]
- Wyjście: true

- Wejście: s = "applepenapple", wordDict = ["apple","pen"]
- Wyjście: true''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def word_break(s, wordDict):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function wordBreak(s, wordDict) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool WordBreak(string s, string[] wordDict) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto wordBreak(const string& s, auto wordDict) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "leetcode,[\"leet\",\"code\"]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "applepenapple,[\"apple\",\"pen\"]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "catsandog,[\"cats\",\"dog\",\"sand\",\"and\",\"cat\"]",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "a,[\"a\"]",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Sposoby Dekodowania''',
            'description': '''Liczby 1-26 reprezentują litery A-Z. Policz ile jest sposobów dekodowania ciągu cyfr.

Przykład:
- Wejście: "12"
- Wyjście: 2 ("AB" lub "L")

- Wejście: "226"
- Wyjście: 3 ("BZ", "VF", "BBF")''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def num_decodings(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function numDecodings(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int NumDecodings(string s) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int numDecodings(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "12",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "226",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "10",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Włamywacz Domów''',
            'description': '''Nie możesz okraść dwóch sąsiednich domów (alarm). Znajdź maksymalną kwotę którą możesz ukraść.

Przykład:
- Wejście: [1,2,3,1]
- Wyjście: 4 (1+3)

- Wejście: [2,7,9,3,1]
- Wyjście: 12 (2+9+1)''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def rob(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function rob(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int Rob(int[] nums) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> rob(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3,1]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[2,7,9,3,1]",
"expected_output": "12",
"is_hidden": False
},
{
"input_data": "[2,1,1,2]",
"expected_output": "4",
"is_hidden": True
},
{
"input_data": "[5]",
"expected_output": "5",
"is_hidden": True
}
],
            'tags': [],
        },
        {
            'title': '''Maksymalny Podciąg''',
            'description': '''Znajdź największą sumę ciągłego podciągu.

Przykład:
- Wejście: [-2,1,-3,4,-1,2,1,-5,4]
- Wyjście: 6 ([4,-1,2,1])

- Wejście: [1]
- Wyjście: 1''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_sub_array(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maxSubArray(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MaxSubArray(int[] nums) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxSubArray(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[-2,1,-3,4,-1,2,1,-5,4]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[5,4,-1,7,8]",
"expected_output": "23",
"is_hidden": True
},
{
"input_data": "[-1]",
"expected_output": "-1",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''K-ty największy element''',
            'description': '''Znajdź k-ty największy element w nieposortowanej tablicy.

Przykład:
- Wejście: nums = [3,2,1,5,6,4], k = 2
- Wyjście: 5

- Wejście: nums = [3,2,3,1,2,4,5,5,6], k = 4
- Wyjście: 4''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_kth_largest(nums, k):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function findKthLargest(nums, k) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findKthLargest(const vector<int>& nums, int k) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3,2,1,5,6,4],2",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "[3,2,3,1,2,4,5,5,6],4",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[1],1",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[7,6,5,4,3,2,1],5",
"expected_output": "3",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Konwersja Zygzak''',
            'description': '''Zapisz string w układzie zygzaka z numRows wierszy i odczytaj linia po linii.

Przykład:
- Wejście: s = "PAYPALISHIRING", numRows = 3
- Wyjście: "PAHNAPLSIIGYIR"
(P   A   H   N
 A P L S I I G
 Y   I   R)

- Wejście: s = "PAYPALISHIRING", numRows = 4
- Wyjście: "PINALSIGYAHRPI"''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def convert(s, numRows):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function convert(s, numRows) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public string Convert(string s, int numRows) {
        // Twój kod tutaj
        return "";
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto convert(const string& s, auto numRows) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "PAYPALISHIRING,3",
"expected_output": "PAHNAPLSIIGYIR",
"is_hidden": False
},
{
"input_data": "PAYPALISHIRING,4",
"expected_output": "PINALSIGYAHRPI",
"is_hidden": False
},
{
"input_data": "A,1",
"expected_output": "A",
"is_hidden": True
},
{
"input_data": "AB,1",
"expected_output": "AB",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Dopasowanie wyrażeń regularnych''',
            'description': '''Zaimplementuj dopasowanie wyrażeń regularnych z obsługą '.' i '*'.
- '.' dopasowuje dowolny pojedynczy znak
- '*' dopasowuje zero lub więcej wystąpień poprzedniego elementu

Przykład:
- Wejście: s = "aa", p = "a"
- Wyjście: false

- Wejście: s = "aa", p = "a*"
- Wyjście: true

- Wejście: s = "ab", p = ".*"
- Wyjście: true''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_match(s, p):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isMatch(s, p) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsMatch(string s, string p) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isMatch(const string& s, auto p) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "aa,a",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "aa,a*",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "ab,.*",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "mississippi,mis*is*p*.",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Mediana dwóch posortowanych tablic''',
            'description': '''Znajdź medianę dwóch posortowanych tablic. Złożoność O(log(m+n)).

Przykład:
- Wejście: nums1 = [1,3], nums2 = [2]
- Wyjście: 2.0

- Wejście: nums1 = [1,2], nums2 = [3,4]
- Wyjście: 2.5''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_median_sorted_arrays(nums1, nums2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function findMedianSortedArrays(nums1, nums2) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        // Twój kod tutaj
        return 0.0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findMedianSortedArrays(auto nums1, auto nums2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,3],[2]",
"expected_output": "2.0",
"is_hidden": False
},
{
"input_data": "[1,2],[3,4]",
"expected_output": "2.5",
"is_hidden": False
},
{
"input_data": "[0,0],[0,0]",
"expected_output": "0.0",
"is_hidden": True
},
{
"input_data": "[],[1]",
"expected_output": "1.0",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Zbieranie Deszczówki''',
            'description': '''Dana jest tablica wysokości słupków. Oblicz ile wody może być zebrane po deszczu.

Przykład:
- Wejście: [0,1,0,2,1,0,1,3,2,1,2,1]
- Wyjście: 6

- Wejście: [4,2,0,3,2,5]
- Wyjście: 9''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def trap(height):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function trap(height) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int Trap(int[] height) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int trap(const vector<int>& height) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[0,1,0,2,1,0,1,3,2,1,2,1]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[4,2,0,3,2,5]",
"expected_output": "9",
"is_hidden": False
},
{
"input_data": "[4,2,3]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[3,0,2,0,4]",
"expected_output": "7",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Problem N-Hetmanów''',
            'description': '''Umieść n hetmanów na szachownicy n×n tak, aby żaden nie atakował drugiego. Zwróć liczbę różnych rozwiązań.

Przykład:
- Wejście: 4
- Wyjście: 2

- Wejście: 1
- Wyjście: 1''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def total_n_queens(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function totalNQueens(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int TotalNQueens(int n) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto totalNQueens(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "4",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "8",
"expected_output": "92",
"is_hidden": True
},
{
"input_data": "5",
"expected_output": "10",
"is_hidden": True
}
],
            'tags': [],
        },
        {
            'title': '''Dopasowanie Wieloznaczników''',
            'description': '''Zaimplementuj dopasowanie z '?' (jeden znak) i '*' (dowolna sekwencja).

Przykład:
- Wejście: s = "aa", p = "a"
- Wyjście: false

- Wejście: s = "aa", p = "*"
- Wyjście: true

- Wejście: s = "cb", p = "?a"
- Wyjście: false''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_match_wildcard(s, p):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isMatchWildcard(s, p) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsMatchWildcard(string s, string p) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isMatchWildcard(const string& s, auto p) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "aa,a",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "aa,*",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "cb,?a",
"expected_output": "False",
"is_hidden": True
},
{
"input_data": "adceb,*a*b",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Najdłuższe Poprawne Nawiasy''',
            'description': '''Znajdź długość najdłuższego poprawnie zagnieżdżonego podciągu nawiasów.

Przykład:
- Wejście: "(()"
- Wyjście: 2

- Wejście: ")()())"
- Wyjście: 4

- Wejście: ""
- Wyjście: 0''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def longest_valid_parentheses(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longestValidParentheses(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int LongestValidParentheses(string s) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto longestValidParentheses(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "(()",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": ")()())",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "(()()",
"expected_output": "4",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Minimalne Okno Podciągu''',
            'description': '''Znajdź minimalne okno w s które zawiera wszystkie znaki z t.

Przykład:
- Wejście: s = "ADOBECODEBANC", t = "ABC"
- Wyjście: "BANC"

- Wejście: s = "a", t = "a"
- Wyjście: "a"''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def min_window(s, t):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function minWindow(s, t) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public string MinWindow(string s, string t) {
        // Twój kod tutaj
        return "";
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int minWindow(const string& s, auto t) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "ADOBECODEBANC,ABC",
"expected_output": "BANC",
"is_hidden": False
},
{
"input_data": "a,a",
"expected_output": "a",
"is_hidden": False
},
{
"input_data": "a,aa",
"expected_output": "",
"is_hidden": True
},
{
"input_data": "ab,b",
"expected_output": "b",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Odległość Edycyjna''',
            'description': '''Oblicz minimalną liczbę operacji (wstaw, usuń, zamień) aby przekształcić word1 w word2.

Przykład:
- Wejście: word1 = "horse", word2 = "ros"
- Wyjście: 3 (horse -> rorse -> rose -> ros)

- Wejście: word1 = "intention", word2 = "execution"
- Wyjście: 5''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def min_distance(word1, word2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function minDistance(word1, word2) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MinDistance(string word1, string word2) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int minDistance(auto word1, auto word2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "horse,ros",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "intention,execution",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": ",",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "a,b",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Maksymalny Prostokąt''',
            'description': '''W macierzy binarnej znajdź obszar największego prostokąta zawierającego tylko jedynki.

Przykład:
- Wejście: [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
- Wyjście: 6

- Wejście: []
- Wyjście: 0''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def maximal_rectangle(matrix):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maximalRectangle(matrix) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MaximalRectangle(char[][] matrix) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> maximalRectangle(const vector<vector<int>>& matrix) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[\"1\",\"0\",\"1\",\"0\",\"0\"],[\"1\",\"0\",\"1\",\"1\",\"1\"],[\"1\",\"1\",\"1\",\"1\",\"1\"],[\"1\",\"0\",\"0\",\"1\",\"0\"]]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[]",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "[[\"0\"]]",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[[\"1\"]]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Różne Podsekwencje''',
            'description': '''Policz ile różnych podsekwencji t występuje w s.

Przykład:
- Wejście: s = "rabbbit", t = "rabbit"
- Wyjście: 3

- Wejście: s = "babgbag", t = "bag"
- Wyjście: 5''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def num_distinct(s, t):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function numDistinct(s, t) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int NumDistinct(string s, string t) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int numDistinct(const string& s, auto t) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "rabbbit,rabbit",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "babgbag,bag",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "b,a",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "aaa,a",
"expected_output": "3",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Rozwiązywanie Sudoku''',
            'description': '''Rozwiąż planszę sudoku 9x9. Pusta komórka to kropka. Zwróć true jeśli rozwiązanie istnieje.

Przykład:
- Wejście: board z częściowo wypełnionymi polami
- Wyjście: true (i wypełniona plansza)''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def solve_sudoku(board):
    # Twój kod tutaj
    # Zwróć True jeśli rozwiązane
    pass''',
            'function_signature_javascript': '''function solveSudoku(board) {
    // Twój kod tutaj
    // Zwróć true jeśli rozwiązane
}''',
            'function_signature_csharp': '''public class Solution {
    public bool SolveSudoku(char[][] board) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> solveSudoku(const vector<vector<int>>& board) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[\"5\",\"3\",\".\",\".\",\"7\",\".\",\".\",\".\",\".\"],[\"6\",\".\",\".\",\"1\",\"9\",\"5\",\".\",\".\",\".\"],[\".\",\"9\",\"8\",\".\",\".\",\".\",\".\",\"6\",\".\"],[\"8\",\".\",\".\",\".\",\"6\",\".\",\".\",\".\",\"3\"],[\"4\",\".\",\".\",\"8\",\".\",\"3\",\".\",\".\",\"1\"],[\"7\",\".\",\".\",\".\",\"2\",\".\",\".\",\".\",\"6\"],[\".\",\"6\",\".\",\".\",\".\",\".\",\"2\",\"8\",\".\"],[\".\",\".\",\".\",\"4\",\"1\",\"9\",\".\",\".\",\"5\"],[\".\",\".\",\".\",\".\",\"8\",\".\",\".\",\"7\",\"9\"]]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "[[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"],[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"],[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"],[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"],[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"],[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"],[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"],[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"],[\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\",\".\"]]",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "[[\"5\",\"3\",\".\",\".\",\"7\",\".\",\".\",\".\",\".\"],[\"6\",\".\",\".\",\"1\",\"9\",\"5\",\".\",\".\",\".\"],[\".\",\"9\",\"8\",\".\",\".\",\".\",\".\",\"6\",\".\"],[\"8\",\".\",\".\",\".\",\"6\",\".\",\".\",\".\",\"3\"],[\"4\",\".\",\".\",\"8\",\".\",\"3\",\".\",\".\",\"1\"],[\"7\",\".\",\".\",\".\",\"2\",\".\",\".\",\".\",\"6\"],[\".\",\"6\",\".\",\".\",\".\",\".\",\"2\",\"8\",\".\"],[\".\",\".\",\".\",\"4\",\"1\",\"9\",\".\",\".\",\"5\"],[\".\",\".\",\".\",\".\",\"8\",\".\",\".\",\"7\",\"9\"]]",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "[[\"1\",\"2\",\"3\",\"4\",\"5\",\"6\",\"7\",\"8\",\"9\"],[\"4\",\"5\",\"6\",\"7\",\"8\",\"9\",\"1\",\"2\",\"3\"],[\"7\",\"8\",\"9\",\"1\",\"2\",\"3\",\"4\",\"5\",\"6\"],[\"2\",\"3\",\"4\",\"5\",\"6\",\"7\",\"8\",\"9\",\"1\"],[\"5\",\"6\",\"7\",\"8\",\"9\",\"1\",\"2\",\"3\",\"4\"],[\"8\",\"9\",\"1\",\"2\",\"3\",\"4\",\"5\",\"6\",\"7\"],[\"3\",\"4\",\"5\",\"6\",\"7\",\"8\",\"9\",\"1\",\"2\"],[\"6\",\"7\",\"8\",\"9\",\"1\",\"2\",\"3\",\"4\",\"5\"],[\"9\",\"1\",\"2\",\"3\",\"4\",\"5\",\"6\",\"7\",\"8\"]]",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': [],
        },
        {
            'title': '''Drabinka Słów II''',
            'description': '''Znajdź wszystkie najkrótsze ścieżki transformacji od beginWord do endWord zmieniając po jednej literze (słowo musi być w wordList).

Przykład:
- Wejście: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
- Wyjście: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

- Wejście: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
- Wyjście: []''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_ladders(beginWord, endWord, wordList):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function findLadders(beginWord, endWord, wordList) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public string[][] FindLadders(string beginWord, string endWord, string[] wordList) {
        // Twój kod tutaj
        return new string[0][];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findLadders(auto beginWord, auto endWord, auto wordList) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hit,cog,[\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]",
"expected_output": "[[\"hit\",\"hot\",\"dot\",\"dog\",\"cog\"],[\"hit\",\"hot\",\"lot\",\"log\",\"cog\"]]",
"is_hidden": False
},
{
"input_data": "hit,cog,[\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]",
"expected_output": "[]",
"is_hidden": False
},
{
"input_data": "a,c,[\"a\",\"b\",\"c\"]",
"expected_output": "[[\"a\",\"c\"]]",
"is_hidden": True
},
{
"input_data": "red,tax,[\"ted\",\"tex\",\"red\",\"tax\",\"tad\",\"den\",\"rex\",\"pee\"]",
"expected_output": "[[\"red\",\"ted\",\"tad\",\"tax\"],[\"red\",\"ted\",\"tex\",\"tax\"],[\"red\",\"rex\",\"tex\",\"tax\"]]",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Największy Prostokąt w Histogramie''',
            'description': '''Znajdź obszar największego prostokąta w histogramie.

Przykład:
- Wejście: [2,1,5,6,2,3]
- Wyjście: 10

- Wejście: [2,4]
- Wyjście: 4''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def largest_rectangle_area(heights):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function largestRectangleArea(heights) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int LargestRectangleArea(int[] heights) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> largestRectangleArea(const vector<int>& heights) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2,1,5,6,2,3]",
"expected_output": "10",
"is_hidden": False
},
{
"input_data": "[2,4]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[2,1,2]",
"expected_output": "3",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Przeplatany ciąg''',
            'description': '''Sprawdź czy s2 jest "scrambled" wersją s1 (rekurencyjne dzielenie i zamienianie).

Przykład:
- Wejście: s1 = "great", s2 = "rgeat"
- Wyjście: true

- Wejście: s1 = "abcde", s2 = "caebd"
- Wyjście: false''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_scramble(s1, s2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isScramble(s1, s2) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsScramble(string s1, string s2) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isScramble(const string& s1, const string& s2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "great,rgeat",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "abcde,caebd",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "a,a",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "abc,bca",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Podział Palindromu II''',
            'description': '''Znajdź minimalną liczbę cięć aby podzielić string na palindromy.

Przykład:
- Wejście: "aab"
- Wyjście: 1 (aa|b)

- Wejście: "a"
- Wyjście: 0

- Wejście: "ab"
- Wyjście: 1''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def min_cut(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function minCut(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MinCut(string s) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int minCut(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "aab",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "a",
"expected_output": "0",
"is_hidden": False
},
{
"input_data": "ab",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "abcba",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Przeplatający ciąg''',
            'description': '''Sprawdź czy s3 jest tworzony przez przeplatanie s1 i s2.

Przykład:
- Wejście: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
- Wyjście: true

- Wejście: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
- Wyjście: false''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_interleave(s1, s2, s3):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isInterleave(s1, s2, s3) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public bool IsInterleave(string s1, string s2, string s3) {
        // Twój kod tutaj
        return false;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isInterleave(const string& s1, const string& s2, const string& s3) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "aabcc,dbbca,aadbbcbcac",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "aabcc,dbbca,aadbbbaccc",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": ",,",
"expected_output": "True",
"is_hidden": True
},
{
"input_data": "a,b,ab",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Wyszukiwanie Słów II''',
            'description': '''Znajdź wszystkie słowa z words które istnieją w planszy. Słowa tworzą się z sąsiadujących komórek.

Przykład:
- Wejście: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
- Wyjście: ["eat","oath"]''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_words(board, words):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function findWords(board, words) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public string[] FindWords(char[][] board, string[] words) {
        // Twój kod tutaj
        return new string[0];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findWords(const vector<vector<int>>& board, const vector<string>& words) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[\"o\",\"a\",\"a\",\"n\"],[\"e\",\"t\",\"a\",\"e\"],[\"i\",\"h\",\"k\",\"r\"],[\"i\",\"f\",\"l\",\"v\"]],[\"oath\",\"pea\",\"eat\",\"rain\"]",
"expected_output": "[\"eat\",\"oath\"]",
"is_hidden": False
},
{
"input_data": "[[\"a\",\"b\"],[\"c\",\"d\"]],[\"abcb\"]",
"expected_output": "[]",
"is_hidden": False
},
{
"input_data": "[[\"a\"]],[\"a\"]",
"expected_output": "[\"a\"]",
"is_hidden": True
},
{
"input_data": "[[\"a\",\"a\"]],[\"aaa\"]",
"expected_output": "[]",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Najlepszy Czas na Kupno/Sprzedaż Akcji III''',
            'description': '''Maksymalizuj zysk z maksymalnie 2 transakcji (kup-sprzedaj).

Przykład:
- Wejście: [3,3,5,0,0,3,1,4]
- Wyjście: 6 (kup w 0, sprzedaj w 3, kup w 3, sprzedaj w 4)

- Wejście: [1,2,3,4,5]
- Wyjście: 4''',
            'difficulty': '''hard''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_profit(prices):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maxProfit(prices) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MaxProfit(int[] prices) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxProfit(const vector<int>& prices) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3,3,5,0,0,3,1,4]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[1,2,3,4,5]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[7,6,4,3,1]",
"expected_output": "0",
"is_hidden": True
},
{
"input_data": "[1]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Liczba Mniejszych Liczb Po Prawej''',
            'description': '''Dla każdego elementu nums[i] znajdź liczbę elementów mniejszych od niego po prawej stronie.

Przykład:
- Wejście: [5,2,6,1]
- Wyjście: [2,1,1,0]

- Wejście: [-1]
- Wyjście: [0]''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def count_smaller(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function countSmaller(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int[] CountSmaller(int[] nums) {
        // Twój kod tutaj
        return new int[0];
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countSmaller(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[5,2,6,1]",
"expected_output": "[2,1,1,0]",
"is_hidden": False
},
{
"input_data": "[-1]",
"expected_output": "[0]",
"is_hidden": False
},
{
"input_data": "[-1,-1]",
"expected_output": "[0,0]",
"is_hidden": True
},
{
"input_data": "[1,2,3,4,5]",
"expected_output": "[0,0,0,0,0]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Przebijanie Balonów''',
            'description': '''Maksymalizuj monety z przebijania balonów. Przebicie balonu i daje nums[i-1] * nums[i] * nums[i+1] monet.

Przykład:
- Wejście: [3,1,5,8]
- Wyjście: 167

- Wejście: [1,5]
- Wyjście: 10''',
            'difficulty': '''hard''',
            'points': 100,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_coins(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maxCoins(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public class Solution {
    public int MaxCoins(int[] nums) {
        // Twój kod tutaj
        return 0;
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxCoins(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3,1,5,8]",
"expected_output": "167",
"is_hidden": False
},
{
"input_data": "[1,5]",
"expected_output": "10",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": True
},
{
"input_data": "[9,76,64,21,97,60]",
"expected_output": "1546860",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Sortowanie szybkie''',
            'description': '''Zaimplementuj algorytm sortowania szybkiego (quick sort).

Posortuj tablicę liczb całkowitych rosnąco używając algorytmu quick sort.

**Przykład:**
- Wejście: [10, 7, 8, 9, 1, 5]
- Wyjście: [1, 5, 7, 8, 9, 10]

**Ograniczenia:**
- 1 <= długość tablicy <= 5 * 10^4
- -10^9 <= element <= 10^9''',
            'difficulty': '''hard''',
            'points': 120,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def quick_sort(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function quickSort(arr) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] QuickSort(int[] arr)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

void quickSort(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[10, 7, 8, 9, 1, 5]",
"expected_output": "[1, 5, 7, 8, 9, 10]",
"is_hidden": False
},
{
"input_data": "[5, 2, 8, 1, 9]",
"expected_output": "[1, 2, 5, 8, 9]",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "[1]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Potęgowanie szybkie''',
            'description': '''Oblicz x^n (x do potęgi n) używając szybkiego potęgowania.

**Przykład:**
- Wejście: x = 2, n = 10
- Wyjście: 1024

- Wejście: x = 2, n = -2
- Wyjście: 0.25

**Ograniczenia:**
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def power(x, n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function power(x, n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static double Power(double x, int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int power(int x, int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "2, 10",
"expected_output": "1024",
"is_hidden": False
},
{
"input_data": "2.1, 3",
"expected_output": "9.261",
"is_hidden": False
},
{
"input_data": "2, 0",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms", "math"],
        },
        {
            'title': '''Rotacja tablicy''',
            'description': '''Obrót tablicę w prawo o k kroków.

**Przykład:**
- Wejście: nums = [1,2,3,4,5,6,7], k = 3
- Wyjście: [5,6,7,1,2,3,4]

- Wejście: nums = [-1,-100,3,99], k = 2
- Wyjście: [3,99,-1,-100]

**Ograniczenia:**
- 1 <= długość tablicy <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def rotate(nums, k):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function rotate(nums, k) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] Rotate(int[] nums, int k)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

void rotate(const vector<int>& nums, int k) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3,4,5,6,7], 3",
"expected_output": "[5,6,7,1,2,3,4]",
"is_hidden": False
},
{
"input_data": "[-1,-100,3,99], 2",
"expected_output": "[3,99,-1,-100]",
"is_hidden": False
},
{
"input_data": "[1,2], 3",
"expected_output": "[2,1]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Usuń duplikaty z posortowanej tablicy''',
            'description': '''Usuń duplikaty z posortowanej tablicy w miejscu i zwróć nową długość.

**Przykład:**
- Wejście: [1,1,2]
- Wyjście: 2, tablica = [1,2,_]

- Wejście: [0,0,1,1,1,2,2,3,3,4]
- Wyjście: 5, tablica = [0,1,2,3,4,_,_,_,_,_]

**Ograniczenia:**
- 0 <= długość tablicy <= 3 * 10^4''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def remove_duplicates(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function removeDuplicates(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int RemoveDuplicates(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> removeDuplicates(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,1,2]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[0,0,1,1,1,2,2,3,3,4]",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "[1,2,3]",
"expected_output": "3",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Wszystkie permutacje''',
            'description': '''Wygeneruj wszystkie możliwe permutacje tablicy liczb.

**Przykład:**
- Wejście: [1,2,3]
- Wyjście: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

**Ograniczenia:**
- 1 <= długość tablicy <= 6
- -10 <= nums[i] <= 10''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def permutations(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function permutations(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<List<int>> Permutations(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> permutations(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3]",
"expected_output": "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "[[1]]",
"is_hidden": False
},
{
"input_data": "[1,2]",
"expected_output": "[[1,2],[2,1]]",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Zliczanie wystąpień znaku''',
            'description': '''Zlicz ile razy każdy znak występuje w ciągu znaków.

Zwróć słownik/obiekt z parami znak: liczba_wystąpień.

**Przykład:**
- Wejście: "hello"
- Wyjście: {"h": 1, "e": 1, "l": 2, "o": 1}

**Ograniczenia:**
- 1 <= długość ciągu <= 10^4''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def count_chars(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function countChars(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static Dictionary<char, int> CountChars(string s)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int countChars(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "hello",
"expected_output": "{\"h\": 1, \"e\": 1, \"l\": 2, \"o\": 1}",
"is_hidden": False
},
{
"input_data": "aaa",
"expected_output": "{\"a\": 3}",
"is_hidden": False
},
{
"input_data": "abc",
"expected_output": "{\"a\": 1, \"b\": 1, \"c\": 1}",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Konwersja liczby rzymskiej''',
            'description': '''Konwertuj liczbę rzymską na liczbę całkowitą.

**Przykład:**
- Wejście: "III"
- Wyjście: 3

- Wejście: "MCMXCIV"
- Wyjście: 1994

**Ograniczenia:**
- 1 <= s.length <= 15
- s zawiera tylko znaki ('I', 'V', 'X', 'L', 'C', 'D', 'M')''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def roman_to_int(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function romanToInt(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int RomanToInt(string s)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int romanToInt(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "III",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "MCMXCIV",
"expected_output": "1994",
"is_hidden": False
},
{
"input_data": "IX",
"expected_output": "9",
"is_hidden": True
}
],
            'tags': ["strings", "math"],
        },
        {
            'title': '''Konwersja na liczbę rzymską''',
            'description': '''Konwertuj liczbę całkowitą na liczbę rzymską.

**Przykład:**
- Wejście: 3
- Wyjście: "III"

- Wejście: 1994
- Wyjście: "MCMXCIV"

**Ograniczenia:**
- 1 <= num <= 3999''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def int_to_roman(num):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function intToRoman(num) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static string IntToRoman(int num)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

string intToRoman(int num) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "3",
"expected_output": "III",
"is_hidden": False
},
{
"input_data": "1994",
"expected_output": "MCMXCIV",
"is_hidden": False
},
{
"input_data": "58",
"expected_output": "LVIII",
"is_hidden": True
}
],
            'tags': ["strings", "math"],
        },
        {
            'title': '''Rotacja macierzy o 90 stopni''',
            'description': '''Obrót macierz n x n o 90 stopni w prawo.

**Przykład:**
- Wejście: [[1,2,3],[4,5,6],[7,8,9]]
- Wyjście: [[7,4,1],[8,5,2],[9,6,3]]

**Ograniczenia:**
- n == matrix.length == matrix[i].length
- 1 <= n <= 20''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def rotate_matrix(matrix):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function rotateMatrix(matrix) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[][] RotateMatrix(int[][] matrix)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

void rotateMatrix(const vector<vector<int>>& matrix) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[1,2,3],[4,5,6],[7,8,9]]",
"expected_output": "[[7,4,1],[8,5,2],[9,6,3]]",
"is_hidden": False
},
{
"input_data": "[[1]]",
"expected_output": "[[1]]",
"is_hidden": False
},
{
"input_data": "[[1,2],[3,4]]",
"expected_output": "[[3,1],[4,2]]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Kompresja ciągu znaków''',
            'description': '''Skompresuj ciąg znaków używając liczby powtórzeń.

Jeśli skompresowany ciąg nie jest krótszy od oryginału, zwróć oryginalny ciąg.

**Przykład:**
- Wejście: "aabcccccaaa"
- Wyjście: "a2b1c5a3"

- Wejście: "abc"
- Wyjście: "abc"

**Ograniczenia:**
- 1 <= s.length <= 10^5''',
            'difficulty': '''medium''',
            'points': 50,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def compress_string(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function compressString(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static string CompressString(string s)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

string compressString(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "aabcccccaaa",
"expected_output": "a2b1c5a3",
"is_hidden": False
},
{
"input_data": "abc",
"expected_output": "abc",
"is_hidden": False
},
{
"input_data": "aabbcc",
"expected_output": "aabbcc",
"is_hidden": True
}
],
            'tags': ["strings"],
        },
        {
            'title': '''Znajdź medianę''',
            'description': '''Znajdź medianę w nieposortowanej tablicy liczb.

Mediana to środkowa wartość w posortowanym zbiorze.

**Przykład:**
- Wejście: [3, 1, 2]
- Wyjście: 2

- Wejście: [3, 1, 2, 4]
- Wyjście: 2.5

**Ograniczenia:**
- 1 <= długość tablicy <= 10^5''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def find_median(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function findMedian(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static double FindMedian(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findMedian(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3, 1, 2]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[3, 1, 2, 4]",
"expected_output": "2.5",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Wchodzenie po schodach''',
            'description': '''Oblicz na ile sposobów można wejść na n schodków.

Możesz wchodzić po 1 lub 2 schodki na raz.

**Przykład:**
- Wejście: 2
- Wyjście: 2
- Wyjaśnienie: 1+1 lub 2

- Wejście: 3
- Wyjście: 3
- Wyjaśnienie: 1+1+1 lub 1+2 lub 2+1

**Ograniczenia:**
- 1 <= n <= 45''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def climb_stairs(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function climbStairs(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int ClimbStairs(int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int climbStairs(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "2",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "3",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "5",
"expected_output": "8",
"is_hidden": True
}
],
            'tags': ["algorithms", "math"],
        },
        {
            'title': '''Największa pojemność kontenera''',
            'description': '''Znajdź dwie linie, które razem z osią X tworzą kontener zawierający najwięcej wody.

**Przykład:**
- Wejście: [1,8,6,2,5,4,8,3,7]
- Wyjście: 49

**Ograniczenia:**
- n >= 2
- 0 <= height[i] <= 10^4''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_area(height):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maxArea(height) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int MaxArea(int[] height)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxArea(const vector<int>& height) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,8,6,2,5,4,8,3,7]",
"expected_output": "49",
"is_hidden": False
},
{
"input_data": "[1,1]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[4,3,2,1,4]",
"expected_output": "16",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Trzy elementy o sumie zero''',
            'description': '''Znajdź wszystkie unikalne trójki w tablicy, które sumują się do zera.

**Przykład:**
- Wejście: [-1,0,1,2,-1,-4]
- Wyjście: [[-1,-1,2],[-1,0,1]]

**Ograniczenia:**
- 0 <= długość tablicy <= 3000
- -10^5 <= nums[i] <= 10^5''',
            'difficulty': '''medium''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def three_sum(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function threeSum(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<List<int>> ThreeSum(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> threeSum(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[-1,0,1,2,-1,-4]",
"expected_output": "[[-1,-1,2],[-1,0,1]]",
"is_hidden": False
},
{
"input_data": "[]",
"expected_output": "[]",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "[]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Wygeneruj nawiasy''',
            'description': '''Wygeneruj wszystkie kombinacje poprawnie zbalansowanych nawiasów dla n par.

**Przykład:**
- Wejście: n = 3
- Wyjście: ["((()))","(()())","(())()","()(())","()()()"]

**Ograniczenia:**
- 1 <= n <= 8''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def generate_parentheses(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function generateParentheses(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<string> GenerateParentheses(int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> generateParentheses(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "3",
"expected_output": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]",
"is_hidden": False
},
{
"input_data": "1",
"expected_output": "[\"()\"]",
"is_hidden": False
},
{
"input_data": "2",
"expected_output": "[\"(())\",\"()()\"]",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Problem plecakowy''',
            'description': '''Rozwiąż klasyczny problem plecakowy 0-1.

Mając wagi i wartości n przedmiotów oraz maksymalną wagę W, wybierz przedmioty aby zmaksymalizować wartość.

**Przykład:**
- Wejście: values = [60,100,120], weights = [10,20,30], W = 50
- Wyjście: 220

**Ograniczenia:**
- 1 <= n <= 100
- 1 <= W <= 1000''',
            'difficulty': '''hard''',
            'points': 140,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def knapsack(values, weights, W):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function knapsack(values, weights, W) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int Knapsack(int[] values, int[] weights, int W)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int knapsack(const vector<int>& values, const vector<int>& weights, auto W) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[60,100,120], [10,20,30], 50",
"expected_output": "220",
"is_hidden": False
},
{
"input_data": "[10,20,30], [1,1,1], 2",
"expected_output": "50",
"is_hidden": False
},
{
"input_data": "[5], [10], 5",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Minimalna suma ścieżki''',
            'description': '''Znajdź ścieżkę z lewego górnego do prawego dolnego rogu siatki, która minimalizuje sumę liczb.

Możesz poruszać się tylko w dół lub w prawo.

**Przykład:**
- Wejście: [[1,3,1],[1,5,1],[4,2,1]]
- Wyjście: 7

**Ograniczenia:**
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200''',
            'difficulty': '''medium''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def min_path_sum(grid):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function minPathSum(grid) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int MinPathSum(int[][] grid)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int minPathSum(const vector<vector<int>>& grid) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[1,3,1],[1,5,1],[4,2,1]]",
"expected_output": "7",
"is_hidden": False
},
{
"input_data": "[[1,2,3],[4,5,6]]",
"expected_output": "12",
"is_hidden": False
},
{
"input_data": "[[1]]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Unikalne ścieżki''',
            'description': '''Oblicz liczbę unikalnych ścieżek z lewego górnego do prawego dolnego rogu siatki m x n.

Możesz poruszać się tylko w dół lub w prawo.

**Przykład:**
- Wejście: m = 3, n = 7
- Wyjście: 28

**Ograniczenia:**
- 1 <= m, n <= 100''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def unique_paths(m, n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function uniquePaths(m, n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int UniquePaths(int m, int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> uniquePaths(int m, int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "3, 7",
"expected_output": "28",
"is_hidden": False
},
{
"input_data": "3, 2",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "1, 1",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms", "math"],
        },
        {
            'title': '''Najdłuższy palindromowy podciąg''',
            'description': '''Znajdź najdłuższy palindromowy podciąg w ciągu znaków.

**Przykład:**
- Wejście: "babad"
- Wyjście: "bab" (lub "aba")

- Wejście: "cbbd"
- Wyjście: "bb"

**Ograniczenia:**
- 1 <= s.length <= 1000''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def longest_palindrome(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longestPalindrome(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static string LongestPalindrome(string s)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int longestPalindrome(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "babad",
"expected_output": "bab",
"is_hidden": False
},
{
"input_data": "cbbd",
"expected_output": "bb",
"is_hidden": False
},
{
"input_data": "a",
"expected_output": "a",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Grupowanie anagramów''',
            'description': '''Pogrupuj anagramy razem z tablicy ciągów znaków.

**Przykład:**
- Wejście: ["eat","tea","tan","ate","nat","bat"]
- Wyjście: [["bat"],["nat","tan"],["ate","eat","tea"]]

**Ograniczenia:**
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def group_anagrams(strs):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function groupAnagrams(strs) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<List<string>> GroupAnagrams(string[] strs)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> groupAnagrams(const vector<string>& strs) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]",
"expected_output": "[[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]",
"is_hidden": False
},
{
"input_data": "[\"\"]",
"expected_output": "[[\"\"]]",
"is_hidden": False
},
{
"input_data": "[\"a\"]",
"expected_output": "[[\"a\"]]",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Iloczyn tablicy poza własnym elementem''',
            'description': '''Zwróć tablicę gdzie każdy element to iloczyn wszystkich elementów poza tym na danym indeksie.

Nie używaj dzielenia i rozwiąż w O(n).

**Przykład:**
- Wejście: [1,2,3,4]
- Wyjście: [24,12,8,6]

**Ograniczenia:**
- 2 <= długość tablicy <= 10^5
- -30 <= nums[i] <= 30''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def product_except_self(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function productExceptSelf(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] ProductExceptSelf(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> productExceptSelf(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3,4]",
"expected_output": "[24,12,8,6]",
"is_hidden": False
},
{
"input_data": "[-1,1,0,-3,3]",
"expected_output": "[0,0,9,0,0]",
"is_hidden": False
},
{
"input_data": "[2,3,4,5]",
"expected_output": "[60,40,30,24]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Brakująca liczba''',
            'description': '''Znajdź brakującą liczbę w tablicy zawierającej n różnych liczb z zakresu [0, n].

**Przykład:**
- Wejście: [3,0,1]
- Wyjście: 2

- Wejście: [9,6,4,2,3,5,7,0,1]
- Wyjście: 8

**Ograniczenia:**
- n == nums.length
- 1 <= n <= 10^4''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def missing_number(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function missingNumber(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int MissingNumber(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int missingNumber(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3,0,1]",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "[9,6,4,2,3,5,7,0,1]",
"expected_output": "8",
"is_hidden": False
},
{
"input_data": "[0,1]",
"expected_output": "2",
"is_hidden": True
}
],
            'tags': ["math", "arrays"],
        },
        {
            'title': '''Sito Eratostenesa''',
            'description': '''Znajdź wszystkie liczby pierwsze mniejsze niż n używając Sita Eratostenesa.

**Przykład:**
- Wejście: 10
- Wyjście: [2,3,5,7]

- Wejście: 20
- Wyjście: [2,3,5,7,11,13,17,19]

**Ograniczenia:**
- 2 <= n <= 5 * 10^6''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def sieve_of_eratosthenes(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function sieveOfEratosthenes(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<int> SieveOfEratosthenes(int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> sieveOfEratosthenes(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "10",
"expected_output": "[2,3,5,7]",
"is_hidden": False
},
{
"input_data": "20",
"expected_output": "[2,3,5,7,11,13,17,19]",
"is_hidden": False
},
{
"input_data": "2",
"expected_output": "[]",
"is_hidden": True
}
],
            'tags': ["algorithms", "math"],
        },
        {
            'title': '''Zbiór potęgowy''',
            'description': '''Wygeneruj wszystkie możliwe podzbiory (zbiór potęgowy) danego zbioru liczb.

**Przykład:**
- Wejście: [1,2,3]
- Wyjście: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

**Ograniczenia:**
- 1 <= nums.length <= 10''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def subsets(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function subsets(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<List<int>> Subsets(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> subsets(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3]",
"expected_output": "[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "[[],[0]]",
"is_hidden": False
},
{
"input_data": "[1,2]",
"expected_output": "[[],[1],[2],[1,2]]",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Kombinacje liter numeru telefonu''',
            'description': '''Zwróć wszystkie możliwe kombinacje liter dla cyfr numeru telefonu.

Mapowanie jak na klawiaturze telefonu (2-ABC, 3-DEF, itd.)

**Przykład:**
- Wejście: "23"
- Wyjście: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Ograniczenia:**
- 0 <= digits.length <= 4
- digits[i] jest cyfrą z zakresu ['2', '9']''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def letter_combinations(digits):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function letterCombinations(digits) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<string> LetterCombinations(string digits)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> letterCombinations(const string& digits) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "23",
"expected_output": "[\"ad\",\"ae\",\"af\",\"bd\",\"be\",\"bf\",\"cd\",\"ce\",\"cf\"]",
"is_hidden": False
},
{
"input_data": "",
"expected_output": "[]",
"is_hidden": False
},
{
"input_data": "2",
"expected_output": "[\"a\",\"b\",\"c\"]",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Przecięcie dwóch tablic''',
            'description': '''Znajdź przecięcie dwóch tablic (wspólne elementy).

**Przykład:**
- Wejście: nums1 = [1,2,2,1], nums2 = [2,2]
- Wyjście: [2,2]

- Wejście: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
- Wyjście: [4,9]

**Ograniczenia:**
- 1 <= nums1.length, nums2.length <= 1000''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def intersect(nums1, nums2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function intersect(nums1, nums2) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] Intersect(int[] nums1, int[] nums2)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> intersect(auto nums1, auto nums2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,2,1], [2,2]",
"expected_output": "[2,2]",
"is_hidden": False
},
{
"input_data": "[4,9,5], [9,4,9,8,4]",
"expected_output": "[4,9]",
"is_hidden": False
},
{
"input_data": "[1], [1]",
"expected_output": "[1]",
"is_hidden": True
}
],
            'tags': ["arrays"],
        },
        {
            'title': '''Suma cyfr liczby''',
            'description': '''Oblicz sumę wszystkich cyfr danej liczby całkowitej.

**Przykład:**
- Wejście: 12345
- Wyjście: 15

- Wejście: 999
- Wyjście: 27

**Ograniczenia:**
- 0 <= n <= 2^31 - 1''',
            'difficulty': '''easy''',
            'points': 20,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def digit_sum(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function digitSum(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int DigitSum(int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int digitSum(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "12345",
"expected_output": "15",
"is_hidden": False
},
{
"input_data": "999",
"expected_output": "27",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Sprawdź liczbę Armstrong''',
            'description': '''Sprawdź czy liczba jest liczbą Armstronga.

Liczba Armstronga to liczba, która jest równa sumie swoich cyfr podniesionych do potęgi równej liczbie cyfr.

**Przykład:**
- Wejście: 153
- Wyjście: true (1³ + 5³ + 3³ = 153)

- Wejście: 123
- Wyjście: false

**Ograniczenia:**
- 0 <= n <= 10^9''',
            'difficulty': '''easy''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def is_armstrong(n):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isArmstrong(n) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static bool IsArmstrong(int n)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isArmstrong(int n) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "153",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "123",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "9",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Najdłuższa wspólna podsekwencja''',
            'description': '''Znajdź długość najdłuższej wspólnej podsekwencji dwóch ciągów znaków.

**Przykład:**
- Wejście: text1 = "abcde", text2 = "ace"
- Wyjście: 3 (podsekwencja "ace")

**Ograniczenia:**
- 1 <= text1.length, text2.length <= 1000''',
            'difficulty': '''medium''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def lcs(text1, text2):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function lcs(text1, text2) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int Lcs(string text1, string text2)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int lcs(auto text1, auto text2) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "abcde, ace",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "abc, abc",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "abc, def",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Znajdź szczyt w górach''',
            'description': '''Znajdź indeks szczytowego elementu w tablicy górskiej.

Tablica górska to tablica, która najpierw rośnie, osiąga szczyt, a następnie maleje.

**Przykład:**
- Wejście: [0,1,0]
- Wyjście: 1

- Wejście: [0,2,1,0]
- Wyjście: 1

**Ograniczenia:**
- 3 <= arr.length <= 10^4''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def peak_index(arr):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function peakIndex(arr) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int PeakIndex(int[] arr)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int peakIndex(const vector<int>& arr) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[0,1,0]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[0,2,1,0]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[0,10,5,2]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Pierwsza i ostatnia pozycja w posortowanej tablicy''',
            'description': '''Znajdź pierwszą i ostatnią pozycję elementu w posortowanej tablicy.

**Przykład:**
- Wejście: nums = [5,7,7,8,8,10], target = 8
- Wyjście: [3,4]

- Wejście: nums = [5,7,7,8,8,10], target = 6
- Wyjście: [-1,-1]

**Ograniczenia:**
- 0 <= nums.length <= 10^5
- Rozwiązanie w O(log n)''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def search_range(nums, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function searchRange(nums, target) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] SearchRange(int[] nums, int target)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int searchRange(const vector<int>& nums, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[5,7,7,8,8,10], 8",
"expected_output": "[3,4]",
"is_hidden": False
},
{
"input_data": "[5,7,7,8,8,10], 6",
"expected_output": "[-1,-1]",
"is_hidden": False
},
{
"input_data": "[], 0",
"expected_output": "[-1,-1]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Najdłuższy rosnący podciąg''',
            'description': '''Znajdź długość najdłuższego rosnącego podciągu w tablicy.

**Przykład:**
- Wejście: [10,9,2,5,3,7,101,18]
- Wyjście: 4 (podciąg [2,3,7,101])

**Ograniczenia:**
- 1 <= nums.length <= 2500''',
            'difficulty': '''medium''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def length_of_lis(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function lengthOfLIS(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int LengthOfLIS(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int lengthOfLis(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[10,9,2,5,3,7,101,18]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[0,1,0,3,2,3]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[7,7,7,7,7,7,7]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Zamiana monet''',
            'description': '''Oblicz minimalną liczbę monet potrzebnych do uzyskania kwoty.

**Przykład:**
- Wejście: coins = [1,2,5], amount = 11
- Wyjście: 3 (11 = 5 + 5 + 1)

**Ograniczenia:**
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def coin_change(coins, amount):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function coinChange(coins, amount) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int CoinChange(int[] coins, int amount)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int coinChange(const vector<int>& coins, int amount) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,5], 11",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[2], 3",
"expected_output": "-1",
"is_hidden": False
},
{
"input_data": "[1], 0",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms"],
        },
        {
            'title': '''Maksymalny kwadrat''',
            'description': '''Znajdź największy kwadrat zawierający same jedynki w binarnej macierzy.

**Przykład:**
- Wejście: [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
- Wyjście: 4

**Ograniczenia:**
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300''',
            'difficulty': '''medium''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def maximal_square(matrix):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maximalSquare(matrix) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int MaximalSquare(char[][] matrix)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> maximalSquare(const vector<vector<int>>& matrix) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[\"1\",\"0\",\"1\",\"0\",\"0\"],[\"1\",\"0\",\"1\",\"1\",\"1\"],[\"1\",\"1\",\"1\",\"1\",\"1\"],[\"1\",\"0\",\"0\",\"1\",\"0\"]]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[[\"0\",\"1\"],[\"1\",\"0\"]]",
"expected_output": "1",
"is_hidden": False
},
{
"input_data": "[[\"0\"]]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Sortowanie kolorów''',
            'description': '''Posortuj tablicę zawierającą tylko 0, 1 i 2 (reprezentujące kolory) w miejscu.

**Przykład:**
- Wejście: [2,0,2,1,1,0]
- Wyjście: [0,0,1,1,2,2]

**Ograniczenia:**
- n == nums.length
- 1 <= n <= 300
- nums[i] to 0, 1 lub 2''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def sort_colors(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function sortColors(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static void SortColors(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

void sortColors(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2,0,2,1,1,0]",
"expected_output": "[0,0,1,1,2,2]",
"is_hidden": False
},
{
"input_data": "[2,0,1]",
"expected_output": "[0,1,2]",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "[0]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Zdekoduj sposoby''',
            'description': '''Oblicz liczbę sposobów dekodowania zakodowanego ciągu znaków.

Mapowanie: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

**Przykład:**
- Wejście: "12"
- Wyjście: 2 ("AB" lub "L")

- Wejście: "226"
- Wyjście: 3 ("BZ", "VF", "BBF")

**Ograniczenia:**
- 1 <= s.length <= 100''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def num_decodings(s):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function numDecodings(s) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int NumDecodings(string s)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int numDecodings(const string& s) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "12",
"expected_output": "2",
"is_hidden": False
},
{
"input_data": "226",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "0",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Najmniejszy wspólny przodek''',
            'description': '''Znajdź najmniejszego wspólnego przodka dwóch węzłów w drzewie binarnym.

**Przykład:**
- Dla drzewa [3,5,1,6,2,0,8,null,null,7,4] i węzłów 5 i 1
- Wyjście: 3

**Ograniczenia:**
- Liczba węzłów: [2, 10^5]
- Wszystkie wartości węzłów są unikalne''',
            'difficulty': '''medium''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def lowest_common_ancestor(root, p, q):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function lowestCommonAncestor(root, p, q) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto lowestCommonAncestor(auto root, auto p, auto q) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[3,5,1,6,2,0,8,None,None,7,4], 5, 1",
"expected_output": "3",
"is_hidden": False
},
{
"input_data": "[3,5,1,6,2,0,8,None,None,7,4], 5, 4",
"expected_output": "5",
"is_hidden": False
},
{
"input_data": "[1,2], 1, 2",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms", "data-structures"],
        },
        {
            'title': '''Najdłuższy ciąg kolejnych elementów''',
            'description': '''Znajdź długość najdłuższego ciągu kolejnych elementów w nieposortowanej tablicy.

**Przykład:**
- Wejście: [100,4,200,1,3,2]
- Wyjście: 4 (ciąg [1,2,3,4])

**Ograniczenia:**
- 0 <= nums.length <= 10^5
- Rozwiązanie w O(n)''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def longest_consecutive(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function longestConsecutive(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int LongestConsecutive(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int longestConsecutive(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[100,4,200,1,3,2]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[0,3,7,2,5,8,4,6,0,1]",
"expected_output": "9",
"is_hidden": False
},
{
"input_data": "[]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Przeszukiwanie w głąb (DFS)''',
            'description': '''Zaimplementuj algorytm przeszukiwania grafu w głąb (DFS) i zwróć kolejność odwiedzania węzłów.

**Przykład:**
- Dla grafu reprezentowanego jako lista sąsiedztwa: [[1,2],[3],[3],[]]
- Startując od węzła 0
- Wyjście: [0,1,3,2]

**Ograniczenia:**
- 1 <= liczba węzłów <= 10^4''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def dfs(graph, start):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function dfs(graph, start) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<int> Dfs(List<List<int>> graph, int start)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> dfs(const unordered_map<int, vector<int>>& graph, int start) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[1,2],[3],[3],[]], 0",
"expected_output": "[0,1,3,2]",
"is_hidden": False
},
{
"input_data": "[[1],[0]], 0",
"expected_output": "[0,1]",
"is_hidden": False
},
{
"input_data": "[[]], 0",
"expected_output": "[0]",
"is_hidden": True
}
],
            'tags': ["algorithms", "data-structures"],
        },
        {
            'title': '''Przeszukiwanie wszerz (BFS)''',
            'description': '''Zaimplementuj algorytm przeszukiwania grafu wszerz (BFS) i zwróć kolejność odwiedzania węzłów.

**Przykład:**
- Dla grafu reprezentowanego jako lista sąsiedztwa: [[1,2],[3],[3],[]]
- Startując od węzła 0
- Wyjście: [0,1,2,3]

**Ograniczenia:**
- 1 <= liczba węzłów <= 10^4''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def bfs(graph, start):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function bfs(graph, start) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<int> Bfs(List<List<int>> graph, int start)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> bfs(const unordered_map<int, vector<int>>& graph, int start) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[1,2],[3],[3],[]], 0",
"expected_output": "[0,1,2,3]",
"is_hidden": False
},
{
"input_data": "[[1],[0]], 0",
"expected_output": "[0,1]",
"is_hidden": False
},
{
"input_data": "[[]], 0",
"expected_output": "[0]",
"is_hidden": True
}
],
            'tags': ["algorithms", "data-structures"],
        },
        {
            'title': '''Odwróć liczbę''',
            'description': '''Odwróć cyfry liczby całkowitej.

**Przykład:**
- Wejście: 123
- Wyjście: 321

- Wejście: -123
- Wyjście: -321

**Ograniczenia:**
- -2^31 <= x <= 2^31 - 1
- Jeśli odwrócona liczba przekracza zakres 32-bitowy, zwróć 0''',
            'difficulty': '''easy''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 1000,
            'memory_limit': 64,
            'function_signature_python': '''def reverse_integer(x):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function reverseInteger(x) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int ReverseInteger(int x)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int reverseInteger(int x) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "123",
"expected_output": "321",
"is_hidden": False
},
{
"input_data": "-123",
"expected_output": "-321",
"is_hidden": False
},
{
"input_data": "120",
"expected_output": "21",
"is_hidden": True
}
],
            'tags': ["math"],
        },
        {
            'title': '''Maksimum w oknie przesuwnym''',
            'description': '''Znajdź maksymalną wartość w każdym oknie przesuwnym o rozmiarze k.

**Przykład:**
- Wejście: nums = [1,3,-1,-3,5,3,6,7], k = 3
- Wyjście: [3,3,5,5,6,7]
- Wyjaśnienie:
  Okno [1 3 -1] -> max = 3
  Okno [3 -1 -3] -> max = 3
  Okno [-1 -3 5] -> max = 5
  itd.

**Ograniczenia:**
- 1 <= nums.length <= 10^5
- 1 <= k <= nums.length''',
            'difficulty': '''medium''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def max_sliding_window(nums, k):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function maxSlidingWindow(nums, k) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] MaxSlidingWindow(int[] nums, int k)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxSlidingWindow(const vector<int>& nums, int k) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,3,-1,-3,5,3,6,7], 3",
"expected_output": "[3,3,5,5,6,7]",
"is_hidden": False
},
{
"input_data": "[1], 1",
"expected_output": "[1]",
"is_hidden": False
},
{
"input_data": "[1,-1], 1",
"expected_output": "[1,-1]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Sortowanie topologiczne''',
            'description': '''Wykonaj sortowanie topologiczne grafu skierowanego acyklicznego (DAG).

**Przykład:**
- Wejście: n = 4, edges = [[1,0],[2,0],[3,1],[3,2]]
- Wyjście: [3,2,1,0] (jedna z możliwych kolejności)

**Ograniczenia:**
- 1 <= n <= 2000
- Graf jest acykliczny''',
            'difficulty': '''medium''',
            'points': 80,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def topological_sort(n, edges):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function topologicalSort(n, edges) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] TopologicalSort(int n, int[][] edges)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> topologicalSort(int n, const vector<vector<int>>& edges) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "4, [[1,0],[2,0],[3,1],[3,2]]",
"expected_output": "[3,2,1,0]",
"is_hidden": False
},
{
"input_data": "2, [[1,0]]",
"expected_output": "[1,0]",
"is_hidden": False
},
{
"input_data": "1, []",
"expected_output": "[0]",
"is_hidden": True
}
],
            'tags': ["algorithms", "data-structures"],
        },
        {
            'title': '''Harmonogram kursów''',
            'description': '''Sprawdź czy można ukończyć wszystkie kursy biorąc pod uwagę zależności.

**Przykład:**
- Wejście: numCourses = 2, prerequisites = [[1,0]]
- Wyjście: true
- Wyjaśnienie: Aby wziąć kurs 1, musisz najpierw ukończyć kurs 0

- Wejście: numCourses = 2, prerequisites = [[1,0],[0,1]]
- Wyjście: false
- Wyjaśnienie: Cykl zależności

**Ograniczenia:**
- 1 <= numCourses <= 2000''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def can_finish(num_courses, prerequisites):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function canFinish(numCourses, prerequisites) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static bool CanFinish(int numCourses, int[][] prerequisites)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool canFinish(int num_courses, const vector<vector<int>>& prerequisites) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "2, [[1,0]]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "2, [[1,0],[0,1]]",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "1, []",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["algorithms", "data-structures"],
        },
        {
            'title': '''Gniące pomarańcze''',
            'description': '''Oblicz minimalny czas potrzebny, aby wszystkie świeże pomarańcze zgnity.

Każdej minuty gniła pomarańcza psuje sąsiednie (góra/dół/lewo/prawo) świeże pomarańcze.

**Przykład:**
- Wejście: [[2,1,1],[1,1,0],[0,1,1]]
- Wyjście: 4
- 0 = puste pole, 1 = świeża pomarańcza, 2 = gniła pomarańcza

**Ograniczenia:**
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10''',
            'difficulty': '''medium''',
            'points': 70,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def oranges_rotting(grid):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function orangesRotting(grid) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int OrangesRotting(int[][] grid)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> orangesRotting(const vector<vector<int>>& grid) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[2,1,1],[1,1,0],[0,1,1]]",
"expected_output": "4",
"is_hidden": False
},
{
"input_data": "[[2,1,1],[0,1,1],[1,0,1]]",
"expected_output": "-1",
"is_hidden": False
},
{
"input_data": "[[0,2]]",
"expected_output": "0",
"is_hidden": True
}
],
            'tags': ["algorithms", "data-structures"],
        },
        {
            'title': '''Sprawdź poprawność Sudoku''',
            'description': '''Sprawdź czy tablica Sudoku 9x9 jest poprawna.

Sudoku jest poprawne jeśli:
- Każdy wiersz zawiera cyfry 1-9 bez powtórzeń
- Każda kolumna zawiera cyfry 1-9 bez powtórzeń
- Każdy podkwadrat 3x3 zawiera cyfry 1-9 bez powtórzeń

**Przykład:**
- Wejście: board (tablica 9x9)
- Wyjście: true lub false

**Ograniczenia:**
- board.length == 9
- board[i].length == 9''',
            'difficulty': '''medium''',
            'points': 60,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def is_valid_sudoku(board):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isValidSudoku(board) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static bool IsValidSudoku(char[][] board)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isValidSudoku(const vector<vector<int>>& board) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[\"5\",\"3\",\".\",\".\",\"7\",\".\",\".\",\".\",\".\"],[\"6\",\".\",\".\",\"1\",\"9\",\"5\",\".\",\".\",\".\"],[\".\",\"9\",\"8\",\".\",\".\",\".\",\".\",\"6\",\".\"],[\"8\",\".\",\".\",\".\",\"6\",\".\",\".\",\".\",\"3\"],[\"4\",\".\",\".\",\"8\",\".\",\"3\",\".\",\".\",\"1\"],[\"7\",\".\",\".\",\".\",\"2\",\".\",\".\",\".\",\"6\"],[\".\",\"6\",\".\",\".\",\".\",\".\",\"2\",\"8\",\".\"],[\".\",\".\",\".\",\"4\",\"1\",\"9\",\".\",\".\",\"5\"],[\".\",\".\",\".\",\".\",\"8\",\".\",\".\",\"7\",\"9\"]]",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "[[\"8\",\"3\",\".\",\".\",\"7\",\".\",\".\",\".\",\".\"],[\"6\",\".\",\".\",\"1\",\"9\",\"5\",\".\",\".\",\".\"],[\".\",\"9\",\"8\",\".\",\".\",\".\",\".\",\"6\",\".\"],[\"8\",\".\",\".\",\".\",\"6\",\".\",\".\",\".\",\"3\"],[\"4\",\".\",\".\",\"8\",\".\",\"3\",\".\",\".\",\"1\"],[\"7\",\".\",\".\",\".\",\"2\",\".\",\".\",\".\",\"6\"],[\".\",\"6\",\".\",\".\",\".\",\".\",\"2\",\"8\",\".\"],[\".\",\".\",\".\",\"4\",\"1\",\"9\",\".\",\".\",\"5\"],[\".\",\".\",\".\",\".\",\"8\",\".\",\".\",\"7\",\"9\"]]",
"expected_output": "False",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Serializacja drzewa binarnego''',
            'description': '''Zaprojektuj algorytm serializacji i deserializacji drzewa binarnego.

**Przykład:**
- Wejście: root = [1,2,3,null,null,4,5]
- serialize(root) -> "1,2,null,null,3,4,null,null,5,null,null"
- deserialize(data) -> [1,2,3,null,null,4,5]

**Ograniczenia:**
- Liczba węzłów: [0, 10^4]''',
            'difficulty': '''medium''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def serialize(root):
    # Twój kod tutaj
    pass

def deserialize(data):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function serialize(root) {
    // Twój kod tutaj
}

function deserialize(data) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static string Serialize(TreeNode root)
{
    // Twój kod tutaj
}

public static TreeNode Deserialize(string data)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto serialize(auto root) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[1,2,3,None,None,4,5]",
"expected_output": "[1,2,3,None,None,4,5]",
"is_hidden": False
},
{
"input_data": "[]",
"expected_output": "[]",
"is_hidden": False
},
{
"input_data": "[1]",
"expected_output": "[1]",
"is_hidden": True
}
],
            'tags': ["algorithms", "data-structures"],
        },
        {
            'title': '''Pamięć podręczna LRU''',
            'description': '''Zaprojektuj strukturę danych LRU (Least Recently Used) cache.

Zaimplementuj metody:
- get(key) - zwraca wartość lub -1
- put(key, value) - wstawia lub aktualizuje wartość

**Przykład:**
- LRUCache(2) - pojemność 2
- put(1, 1)
- put(2, 2)
- get(1) -> 1
- put(3, 3) - usuwa klucz 2
- get(2) -> -1

**Ograniczenia:**
- 1 <= capacity <= 3000
- 0 <= key <= 10^4''',
            'difficulty': '''medium''',
            'points': 90,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''class LRUCache:
    def __init__(self, capacity):
        # Twój kod tutaj
        pass
    
    def get(self, key):
        # Twój kod tutaj
        pass
    
    def put(self, key, value):
        # Twój kod tutaj
        pass''',
            'function_signature_javascript': '''class LRUCache {
    constructor(capacity) {
        // Twój kod tutaj
    }
    
    get(key) {
        // Twój kod tutaj
    }
    
    put(key, value) {
        // Twój kod tutaj
    }
}''',
            'function_signature_csharp': '''public class LRUCache
{
    public LRUCache(int capacity)
    {
        // Twój kod tutaj
    }
    
    public int Get(int key)
    {
        // Twój kod tutaj
    }
    
    public void Put(int key, int value)
    {
        // Twój kod tutaj
    }
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

auto Init(int capacity) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "2, [put(1,1),put(2,2),get(1),put(3,3),get(2)]",
"expected_output": "[None,None,1,None,-1]",
"is_hidden": False
},
{
"input_data": "1, [put(2,1),get(2)]",
"expected_output": "[None,1]",
"is_hidden": True
}
],
            'tags': ["data-structures"],
        },
        {
            'title': '''Zbieranie wody deszczowej''',
            'description': '''Oblicz ile wody może zostać zebrane po deszczu w strukturze reprezentowanej przez tablicę wysokości.

**Przykład:**
- Wejście: [0,1,0,2,1,0,1,3,2,1,2,1]
- Wyjście: 6
- Wyjaśnienie: Można zebrać 6 jednostek wody

**Ograniczenia:**
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5''',
            'difficulty': '''hard''',
            'points': 140,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def trap(height):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function trap(height) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int Trap(int[] height)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int trap(const vector<int>& height) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[0,1,0,2,1,0,1,3,2,1,2,1]",
"expected_output": "6",
"is_hidden": False
},
{
"input_data": "[4,2,0,3,2,5]",
"expected_output": "9",
"is_hidden": False
},
{
"input_data": "[4,2,3]",
"expected_output": "1",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''Word Search II''',
            'description': '''Znajdź wszystkie słowa z listy, które istnieją na planszy.

Słowa mogą być tworzone z liter sąsiadujących komórek (góra/dół/lewo/prawo). Ta sama komórka nie może być użyta więcej niż raz w jednym słowie.

**Przykład:**
- Wejście: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
- Wyjście: ["eat","oath"]

**Ograniczenia:**
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- 1 <= words.length <= 3 * 10^4''',
            'difficulty': '''hard''',
            'points': 160,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 5000,
            'memory_limit': 256,
            'function_signature_python': '''def find_words(board, words):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function findWords(board, words) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<string> FindWords(char[][] board, string[] words)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findWords(const vector<vector<int>>& board, const vector<string>& words) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[[\"o\",\"a\",\"a\",\"n\"],[\"e\",\"t\",\"a\",\"e\"],[\"i\",\"h\",\"k\",\"r\"],[\"i\",\"f\",\"l\",\"v\"]], [\"oath\",\"pea\",\"eat\",\"rain\"]",
"expected_output": "[\"eat\",\"oath\"]",
"is_hidden": False
},
{
"input_data": "[[\"a\",\"b\"],[\"c\",\"d\"]], [\"abcb\"]",
"expected_output": "[]",
"is_hidden": False
},
{
"input_data": "[[\"a\"]], [\"a\"]",
"expected_output": "[\"a\"]",
"is_hidden": True
}
],
            'tags': ["algorithms", "data-structures"],
        },
        {
            'title': '''Przeplatanie ciągów''',
            'description': '''Sprawdź czy ciąg s3 może zostać utworzony przez przeplatanie ciągów s1 i s2.

**Przykład:**
- Wejście: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
- Wyjście: true

- Wejście: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
- Wyjście: false

**Ograniczenia:**
- 0 <= s1.length, s2.length <= 100
- s3.length == s1.length + s2.length''',
            'difficulty': '''hard''',
            'points': 140,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def is_interleave(s1, s2, s3):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function isInterleave(s1, s2, s3) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static bool IsInterleave(string s1, string s2, string s3)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isInterleave(const string& s1, const string& s2, const string& s3) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "aabcc, dbbca, aadbbcbcac",
"expected_output": "True",
"is_hidden": False
},
{
"input_data": "aabcc, dbbca, aadbbbaccc",
"expected_output": "False",
"is_hidden": False
},
{
"input_data": "\"\", \"\", \"\"",
"expected_output": "True",
"is_hidden": True
}
],
            'tags': ["algorithms", "strings"],
        },
        {
            'title': '''Two Sum''',
            'description': '''Znajdź dwa indeksy w tablicy, których elementy sumują się do podanej liczby.

Zwróć tablicę z dwoma indeksami. Każdy element może być użyty tylko raz.

**Przykład:**
- Wejście: nums = [2, 7, 11, 15], target = 9
- Wyjście: [0, 1]
- Wyjaśnienie: nums[0] + nums[1] = 2 + 7 = 9

**Ograniczenia:**
- 2 <= długość tablicy <= 10^4
- -10^9 <= nums[i] <= 10^9
- Tylko jedno poprawne rozwiązanie istnieje''',
            'difficulty': '''medium''',
            'points': 30,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 2000,
            'memory_limit': 128,
            'function_signature_python': '''def two_sum(nums, target):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function twoSum(nums, target) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static int[] TwoSum(int[] nums, int target)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> twoSum(const vector<int>& nums, int target) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[2, 7, 11, 15], 9",
"expected_output": "[0, 1]",
"is_hidden": False
},
{
"input_data": "[3, 2, 4], 6",
"expected_output": "[1, 2]",
"is_hidden": False
},
{
"input_data": "[3, 3], 6",
"expected_output": "[0, 1]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
        {
            'title': '''3Sum''',
            'description': '''Znajdź wszystkie unikalne trójki w tablicy, które sumują się do zera.

**Przykład:**
- Wejście: [-1,0,1,2,-1,-4]
- Wyjście: [[-1,-1,2],[-1,0,1]]

**Ograniczenia:**
- 0 <= długość tablicy <= 3000
- -10^5 <= nums[i] <= 10^5''',
            'difficulty': '''medium''',
            'points': 40,
            'languages': '''python,javascript,csharp,cpp''',
            'time_limit': 3000,
            'memory_limit': 256,
            'function_signature_python': '''def three_sum(nums):
    # Twój kod tutaj
    pass''',
            'function_signature_javascript': '''function threeSum(nums) {
    // Twój kod tutaj
}''',
            'function_signature_csharp': '''public static List<List<int>> ThreeSum(int[] nums)
{
    // Twój kod tutaj
}''',
            'function_signature_cpp': '''#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> threeSum(const vector<int>& nums) {
    // Twój kod tutaj

}''',
            'test_cases': [
{
"input_data": "[-1,0,1,2,-1,-4]",
"expected_output": "[[-1,-1,2],[-1,0,1]]",
"is_hidden": False
},
{
"input_data": "[]",
"expected_output": "[]",
"is_hidden": False
},
{
"input_data": "[0]",
"expected_output": "[]",
"is_hidden": True
}
],
            'tags': ["algorithms", "arrays"],
        },
    ]

    # Create problems
    print(f"\n🔨 Creating {len(problems_data)} problems...")
    created_count = 0
    updated_count = 0

    for idx, problem_data in enumerate(problems_data, 1):
        test_cases_data = problem_data.pop('test_cases')
        tag_slugs = problem_data.pop('tags')

        slug = slugify(problem_data['title'])

        # Check if problem exists
        try:
            problem = Problem.objects.get(slug=slug)
            # Update existing
            for key, value in problem_data.items():
                setattr(problem, key, value)
            problem.created_by = admin_user
            problem.save()

            # Delete old test cases
            problem.test_cases.all().delete()
            updated_count += 1
            status = "🔄"
        except Problem.DoesNotExist:
            # Create new
            problem = Problem.objects.create(
                slug=slug,
                created_by=admin_user,
                **problem_data
            )
            created_count += 1
            status = "✅"

        # Add test cases
        for order, tc_data in enumerate(test_cases_data):
            TestCase.objects.create(
                problem=problem,
                order=order,
                **tc_data
            )

        # Add tags
        problem.tags.clear()
        for tag_slug in tag_slugs:
            if tag_slug in tags:
                problem.tags.add(tags[tag_slug])

        if idx % 10 == 0 or idx == len(problems_data):
            print(f"  {status} Processed {idx}/{len(problems_data)}: {problem.title[:50]}")

    # Final statistics
    total = Problem.objects.count()
    total_points = sum(p.points for p in Problem.objects.all())
    easy_count = Problem.objects.filter(difficulty='easy').count()
    medium_count = Problem.objects.filter(difficulty='medium').count()
    hard_count = Problem.objects.filter(difficulty='hard').count()

    print("\n" + "=" * 80)
    print("🎉 DEPLOYMENT COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print(f"\n📊 Summary:")
    print(f"   ✅ Created: {created_count} problems")
    print(f"   🔄 Updated: {updated_count} problems")
    print(f"   📦 Total: {total} problems")
    print(f"\n📈 By difficulty:")
    print(f"   ✅ Easy: {easy_count}")
    print(f"   ⚡ Medium: {medium_count}")
    print(f"   🔥 Hard: {hard_count}")
    print(f"\n🏆 Total points: {total_points:,}")
    print(f"\n🔗 Access:")
    print(f"   API: /api/problems/")
    print(f"   Admin: /admin/")
    print("=" * 80)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
