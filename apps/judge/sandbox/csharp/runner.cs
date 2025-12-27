#!/usr/bin/env dotnet-script
/**
 * C# sandbox runner for executing user code safely.
 */

using System;
using System.IO;
using System.Text.Json;
using System.Diagnostics;
using System.Threading;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Get code from stdin or environment
            string code = Console.IsInputRedirected
                ? Console.In.ReadToEnd()
                : Environment.GetEnvironmentVariable("CODE") ?? "";

            // Get test input
            string testInput = Environment.GetEnvironmentVariable("TEST_INPUT") ?? "";

            // Get time limit
            int timeLimit = int.Parse(Environment.GetEnvironmentVariable("TIME_LIMIT") ?? "2000");

            // Set timeout
            var cts = new CancellationTokenSource();
            cts.CancelAfter(timeLimit);

            // Execute code
            RunCode(code, testInput, cts.Token);
        }
        catch (OperationCanceledException)
        {
            Console.Error.WriteLine("Time limit exceeded");
            Environment.Exit(124);
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"Runtime error: {ex.Message}");
            Environment.Exit(1);
        }
    }

    static void RunCode(string code, string testInput, CancellationToken cancellationToken)
    {
        try
        {
            // Parse test input
            object inputData;
            try
            {
                inputData = JsonSerializer.Deserialize<object>(testInput);
            }
            catch
            {
                inputData = testInput;
            }

            // Note: In production, you would use Roslyn to compile and execute C# code
            // This is a simplified version
            // For now, we'll just evaluate the code directly

            // Execute the user code
            // This would need proper implementation with Roslyn compiler
            Console.WriteLine("C# execution requires Roslyn compiler integration");

        }
        catch (Exception ex)
        {
            throw new Exception($"Execution error: {ex.Message}");
        }
    }
}
