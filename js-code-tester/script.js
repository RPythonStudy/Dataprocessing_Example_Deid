(function () {
    const editor = document.getElementById('code-editor');
    const runBtn = document.getElementById('run-btn');
    const clearBtn = document.getElementById('clear-btn');
    const clearConsoleBtn = document.getElementById('clear-console-btn');
    const consoleOutput = document.getElementById('console-output');

    // Store original console methods
    const originalConsole = {
        log: console.log,
        error: console.error,
        warn: console.warn,
        info: console.info
    };

    /**
     * Appends a message to the UI console
     */
    function appendToConsole(type, ...args) {
        const line = document.createElement('div');
        line.className = `console-line ${type}`;

        const time = document.createElement('span');
        time.className = 'console-time';
        time.textContent = new Date().toLocaleTimeString('ko-KR', { hour12: false });

        const msg = document.createElement('span');
        msg.className = 'console-msg';
        msg.textContent = args.map(arg => {
            if (typeof arg === 'object') {
                try {
                    return JSON.stringify(arg, null, 2);
                } catch (e) {
                    return String(arg);
                }
            }
            return String(arg);
        }).join(' ');

        line.appendChild(time);
        line.appendChild(msg);
        consoleOutput.appendChild(line);

        // Auto scroll to bottom
        consoleOutput.scrollTop = consoleOutput.scrollHeight;

        // Still log to real browser console
        originalConsole[type].apply(console, args);
    }

    // Override console methods
    console.log = (...args) => appendToConsole('log', ...args);
    console.error = (...args) => appendToConsole('error', ...args);
    console.warn = (...args) => appendToConsole('warn', ...args);
    console.info = (...args) => appendToConsole('info', ...args);

    /**
     * Executes the code
     */
    function runCode() {
        const code = editor.value;
        if (!code.trim()) return;

        console.info('--- Running Script ---');

        try {
            // Using Function constructor is slightly safer than eval but still powerful
            // We use a new Function to execute the code
            const execute = new Function(code);
            execute();
        } catch (err) {
            console.error('Runtime Error:', err.message);
        }
    }

    // Event Listeners
    runBtn.addEventListener('click', runCode);

    clearBtn.addEventListener('click', () => {
        editor.value = '';
        editor.focus();
    });

    clearConsoleBtn.addEventListener('click', () => {
        consoleOutput.innerHTML = '';
        console.info('Console cleared.');
    });

    // Keyboard Shortcuts
    editor.addEventListener('keydown', (e) => {
        // Run with Cmd+Enter or Ctrl+Enter
        if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
            e.preventDefault();
            runCode();
        }

        // Support Tab key in textarea
        if (e.key === 'Tab') {
            e.preventDefault();
            const start = editor.selectionStart;
            const end = editor.selectionEnd;

            // Set textarea value to: text before caret + tab + text after caret
            editor.value = editor.value.substring(0, start) + "    " + editor.value.substring(end);

            // Put caret at right position again
            editor.selectionStart = editor.selectionEnd = start + 4;
        }
    });

    // Initial focus
    editor.focus();
})();
