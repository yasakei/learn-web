# learn-web 🌐

A simple course to teach you all the basics of Web!

Interactive, with Python CLI tool - complete tasks, run verification scripts, and get scores! 

## Features

- 📚 **Interactive Learning**: Step-by-step lessons covering HTML, CSS, and JavaScript basics
- 🎯 **Task-Based Learning**: Complete hands-on coding tasks to progress
- ✅ **Automatic Verification**: Built-in verification system checks your code
- 📊 **Progress Tracking**: Track your score and completion status
- 🔄 **Persistent Progress**: Your progress is saved between sessions

## Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yasakei/learn-web.git
   cd learn-web
   ```

2. Run the learning tool:
   ```bash
   python learn_web.py help
   ```

## Usage

The learn-web tool provides several commands to help you learn web development:

### Basic Commands

```bash
# Show available lessons
python learn_web.py lessons

# Show current lesson and tasks
python learn_web.py current

# Show your progress
python learn_web.py progress

# Verify a completed task
python learn_web.py verify --task <task_id>

# Reset all progress
python learn_web.py reset

# Show help
python learn_web.py help
```

## Learning Path

### Lesson 1: HTML Basics 📄
Learn the fundamentals of HTML structure
- **Task**: Create Basic HTML Structure
- **Goal**: Create an HTML file with proper structure (html, head, body tags)
- **Points**: 10

### Lesson 2: CSS Styling 🎨
Learn how to style HTML with CSS  
- **Task**: Add CSS Styling
- **Goal**: Create a CSS file and demonstrate CSS syntax
- **Points**: 15

### Lesson 3: JavaScript Basics ⚡
Add interactivity with JavaScript
- **Task**: Add JavaScript
- **Goal**: Create a JavaScript file with a function
- **Points**: 20

## Example Workflow

1. **Start learning**:
   ```bash
   python learn_web.py current
   ```

2. **Create your HTML file** (e.g., `index.html`):
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <title>My Page</title>
   </head>
   <body>
       <h1>Hello World!</h1>
   </body>
   </html>
   ```

3. **Verify your work**:
   ```bash
   python learn_web.py verify --task html_basic_structure
   ```

4. **Check your progress**:
   ```bash
   python learn_web.py progress
   ```

5. **Continue to next lesson**:
   ```bash
   python learn_web.py current
   ```

## Testing

Run the test suite to verify everything works correctly:

```bash
python -m unittest test_learn_web.py -v
```

## Progress Tracking

Your progress is automatically saved in `progress.json`. The system tracks:
- ✅ Completed tasks
- 📊 Current score  
- 📖 Current lesson
- 🎯 Overall completion percentage

## File Validation

The tool automatically validates your code files:
- **HTML files**: Checks for proper HTML structure (html, head, body tags)
- **CSS files**: Validates CSS syntax and rules
- **JavaScript files**: Looks for function declarations

## Tips for Success

1. 💡 **Follow the hints**: Each task provides helpful hints
2. 📁 **Use proper file extensions**: `.html`, `.css`, `.js`
3. 🔍 **Check current tasks**: Use `python learn_web.py current` to see what you need to do
4. 📊 **Track progress**: Regular check your progress with `python learn_web.py progress`

## Contributing

Feel free to contribute by:
- Adding new lessons
- Improving task validation
- Enhancing the user interface
- Adding more comprehensive tests

Happy learning! 🚀
