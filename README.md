# learn-web 🌐

A comprehensive course to teach you all the essentials of Web Development!

Interactive Python CLI tool with progressive lessons - complete tasks, run verification scripts, and get scores as you master HTML, CSS, JavaScript, and modern web development techniques from beginner to intermediate level. 

## Features

- 📚 **Comprehensive Learning**: 10 progressive lessons covering HTML, CSS, and JavaScript from basics to advanced
- 🎯 **Task-Based Learning**: 30 hands-on coding tasks to build real skills
- ✅ **Automatic Verification**: Built-in verification system checks your code
- 📊 **Progress Tracking**: Track your score and completion status (530 total points)
- 🔄 **Persistent Progress**: Your progress is saved between sessions
- 🏗️ **Project-Based**: Culminates in building a complete web application

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
- **Task 1**: Create Basic HTML Structure (10 points)
- **Task 2**: Add Semantic HTML Elements (15 points)  
- **Task 3**: Add Content Elements (10 points)

### Lesson 2: CSS Styling 🎨
Learn how to style HTML with CSS
- **Task 1**: Add CSS Styling (15 points)
- **Task 2**: Use CSS Selectors and Properties (15 points)
- **Task 3**: Apply Box Model Properties (15 points)

### Lesson 3: JavaScript Basics ⚡
Add interactivity with JavaScript
- **Task 1**: Add JavaScript (20 points)
- **Task 2**: Use Variables and Operators (15 points)
- **Task 3**: Add Control Structures (20 points)

### Lesson 4: HTML Forms 📋
Learn to create interactive forms
- **Task 1**: Create a Basic Form (20 points)
- **Task 2**: Add Different Input Types (15 points)
- **Task 3**: Add Form Validation (15 points)

### Lesson 5: CSS Layout 📐
Master CSS layout techniques
- **Task 1**: Use Flexbox Layout (25 points)
- **Task 2**: Use CSS Grid (25 points)
- **Task 3**: Make Responsive Design (20 points)

### Lesson 6: JavaScript DOM 🌐
Manipulate the Document Object Model
- **Task 1**: Select DOM Elements (20 points)
- **Task 2**: Manipulate DOM Elements (25 points)
- **Task 3**: Handle Events (25 points)

### Lesson 7: JavaScript ES6+ 🚀
Learn modern JavaScript features
- **Task 1**: Use Arrow Functions (15 points)
- **Task 2**: Use Destructuring (20 points)
- **Task 3**: Use Template Literals (15 points)

### Lesson 8: CSS Advanced 🎭
Advanced CSS techniques and animations
- **Task 1**: Add CSS Transitions (20 points)
- **Task 2**: Create CSS Animations (25 points)
- **Task 3**: Apply CSS Transforms (20 points)

### Lesson 9: JavaScript APIs 🔗
Work with browser APIs and async programming
- **Task 1**: Use Fetch API (30 points)
- **Task 2**: Use Async/Await (25 points)
- **Task 3**: Use Local Storage (20 points)

### Lesson 10: Web Project 🏗️
Build a complete web application
- **Task 1**: Create Project Structure (15 points)
- **Task 2**: Add Interactive Features (35 points)
- **Task 3**: Apply Professional Styling (25 points)

**Total: 10 lessons, 30 tasks, 530 points**

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
- **HTML files**: Checks for proper HTML structure, semantic elements, forms, and content
- **CSS files**: Validates CSS syntax, selectors, layout techniques, and animations
- **JavaScript files**: Looks for functions, variables, control structures, DOM manipulation, and ES6+ features

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
