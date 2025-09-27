#!/usr/bin/env python3
"""
learn-web: An interactive Python CLI tool for learning web development basics
"""

import argparse
import json
import os
import sys
from typing import Dict, List, Optional
import re


class Course:
    """Main course management class"""
    
    def __init__(self):
        self.current_lesson = 0
        self.completed_tasks = set()
        self.score = 0
        self.lessons = self._load_lessons()
        self.progress_file = "progress.json"
        self._load_progress()
    
    def _load_lessons(self) -> List[Dict]:
        """Load lesson definitions"""
        return [
            {
                "id": 1,
                "title": "HTML Basics",
                "description": "Learn the fundamentals of HTML structure",
                "tasks": [
                    {
                        "id": "html_basic_structure",
                        "title": "Create Basic HTML Structure",
                        "description": "Create an HTML file with basic structure (html, head, body tags)",
                        "points": 10,
                        "file_pattern": r".*\.html$",
                        "validation_regex": r"<html.*?>.*<head.*?>.*</head>.*<body.*?>.*</body>.*</html>",
                        "hint": "Use <!DOCTYPE html>, <html>, <head>, <title>, and <body> tags"
                    },
                    {
                        "id": "html_semantic_elements",
                        "title": "Add Semantic HTML Elements",
                        "description": "Add semantic elements like header, nav, main, section, and footer",
                        "points": 15,
                        "file_pattern": r".*\.html$",
                        "validation_regex": r"<header.*?>.*</header>.*<main.*?>.*</main>.*<footer.*?>.*</footer>",
                        "hint": "Use semantic HTML5 elements: <header>, <nav>, <main>, <section>, <footer>"
                    },
                    {
                        "id": "html_content_elements",
                        "title": "Add Content Elements",
                        "description": "Add headings (h1-h6), paragraphs, lists, and links",
                        "points": 10,
                        "file_pattern": r".*\.html$",
                        "validation_regex": r"<h[1-6].*?>.*</h[1-6]>.*<p.*?>.*</p>.*<ul.*?>.*<li.*?>.*</li>.*</ul>.*<a.*?>.*</a>",
                        "hint": "Include headings (h1-h6), paragraphs (p), lists (ul/ol with li), and links (a)"
                    }
                ]
            },
            {
                "id": 2,
                "title": "CSS Styling",
                "description": "Learn how to style HTML with CSS",
                "tasks": [
                    {
                        "id": "css_basic_styling",
                        "title": "Add CSS Styling",
                        "description": "Create a CSS file and link it to your HTML",
                        "points": 15,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*{.*}.*",
                        "hint": "Create a .css file and link it with <link> tag in HTML head"
                    },
                    {
                        "id": "css_selectors_properties",
                        "title": "Use CSS Selectors and Properties",
                        "description": "Style elements using different selectors and common properties",
                        "points": 15,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*\..*{.*}.*#.*{.*}.*",
                        "hint": "Use class selectors (.class) and ID selectors (#id) with CSS properties"
                    },
                    {
                        "id": "css_box_model",
                        "title": "Apply Box Model Properties",
                        "description": "Use margin, padding, border, and width/height properties",
                        "points": 15,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*(margin|padding|border).*:.*",
                        "hint": "Use box model properties: margin, padding, border, width, height"
                    }
                ]
            },
            {
                "id": 3,
                "title": "JavaScript Basics",
                "description": "Add interactivity with JavaScript",
                "tasks": [
                    {
                        "id": "js_basic_script",
                        "title": "Add JavaScript",
                        "description": "Create a JavaScript file with a simple function",
                        "points": 20,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r"function\s+\w+\s*\(.*\)\s*{.*}",
                        "hint": "Create a .js file with a function declaration"
                    },
                    {
                        "id": "js_variables_operators",
                        "title": "Use Variables and Operators",
                        "description": "Declare variables and use basic operators",
                        "points": 15,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*(let|const|var)\s+\w+.*[+\-*/].*",
                        "hint": "Use let/const/var to declare variables and +, -, *, / operators"
                    },
                    {
                        "id": "js_control_structures",
                        "title": "Add Control Structures",
                        "description": "Use if statements and loops",
                        "points": 20,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*if\s*\(.*\)\s*{.*}.*(for|while)\s*\(.*\)\s*{.*}",
                        "hint": "Use if statements and for/while loops"
                    }
                ]
            },
            {
                "id": 4,
                "title": "HTML Forms",
                "description": "Learn to create interactive forms",
                "tasks": [
                    {
                        "id": "html_basic_form",
                        "title": "Create a Basic Form",
                        "description": "Create a form with input fields and submit button",
                        "points": 20,
                        "file_pattern": r".*\.html$",
                        "validation_regex": r"<form.*?>.*<input.*?>.*<button.*?>.*</button>.*</form>",
                        "hint": "Use <form>, <input>, and <button> elements"
                    },
                    {
                        "id": "html_form_inputs",
                        "title": "Add Different Input Types",
                        "description": "Use various input types: text, email, password, number",
                        "points": 15,
                        "file_pattern": r".*\.html$",
                        "validation_regex": r".*type\s*=\s*[\"']?(text|email|password|number)[\"']?.*",
                        "hint": "Use different input types: text, email, password, number"
                    },
                    {
                        "id": "html_form_validation",
                        "title": "Add Form Validation",
                        "description": "Add HTML5 validation attributes like required, pattern",
                        "points": 15,
                        "file_pattern": r".*\.html$",
                        "validation_regex": r".*(required|pattern).*",
                        "hint": "Use HTML5 validation: required, pattern, min, max attributes"
                    }
                ]
            },
            {
                "id": 5,
                "title": "CSS Layout",
                "description": "Master CSS layout techniques",
                "tasks": [
                    {
                        "id": "css_flexbox",
                        "title": "Use Flexbox Layout",
                        "description": "Create layouts using CSS Flexbox",
                        "points": 25,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*display\s*:\s*flex.*",
                        "hint": "Use display: flex and flexbox properties like justify-content, align-items"
                    },
                    {
                        "id": "css_grid",
                        "title": "Use CSS Grid",
                        "description": "Create complex layouts with CSS Grid",
                        "points": 25,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*display\s*:\s*grid.*",
                        "hint": "Use display: grid and grid properties like grid-template-columns"
                    },
                    {
                        "id": "css_responsive",
                        "title": "Make Responsive Design",
                        "description": "Use media queries for responsive design",
                        "points": 20,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*@media.*screen.*",
                        "hint": "Use @media queries to create responsive layouts"
                    }
                ]
            },
            {
                "id": 6,
                "title": "JavaScript DOM",
                "description": "Manipulate the Document Object Model",
                "tasks": [
                    {
                        "id": "js_dom_selection",
                        "title": "Select DOM Elements",
                        "description": "Use methods to select HTML elements",
                        "points": 20,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*(getElementById|querySelector).*",
                        "hint": "Use getElementById, querySelector, or querySelectorAll"
                    },
                    {
                        "id": "js_dom_manipulation",
                        "title": "Manipulate DOM Elements",
                        "description": "Change element content, attributes, and styles",
                        "points": 25,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*(innerHTML|textContent|style\.|setAttribute).*",
                        "hint": "Use innerHTML, textContent, style properties, or setAttribute"
                    },
                    {
                        "id": "js_event_handling",
                        "title": "Handle Events",
                        "description": "Add event listeners to elements",
                        "points": 25,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*addEventListener.*",
                        "hint": "Use addEventListener to handle click, input, or other events"
                    }
                ]
            },
            {
                "id": 7,
                "title": "JavaScript ES6+",
                "description": "Learn modern JavaScript features",
                "tasks": [
                    {
                        "id": "js_arrow_functions",
                        "title": "Use Arrow Functions",
                        "description": "Write functions using arrow function syntax",
                        "points": 15,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*=>\s*{.*}",
                        "hint": "Use arrow function syntax: (param) => { code }"
                    },
                    {
                        "id": "js_destructuring",
                        "title": "Use Destructuring",
                        "description": "Destructure arrays and objects",
                        "points": 20,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*(const|let)\s*{\s*\w+.*}\s*=.*",
                        "hint": "Use destructuring: const {prop} = object or const [item] = array"
                    },
                    {
                        "id": "js_template_literals",
                        "title": "Use Template Literals",
                        "description": "Use template literals for string interpolation",
                        "points": 15,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*`.*\$\{.*\}.*`",
                        "hint": "Use backticks and ${} for template literals: `Hello ${name}`"
                    }
                ]
            },
            {
                "id": 8,
                "title": "CSS Advanced",
                "description": "Advanced CSS techniques and animations",
                "tasks": [
                    {
                        "id": "css_transitions",
                        "title": "Add CSS Transitions",
                        "description": "Create smooth transitions between states",
                        "points": 20,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*transition\s*:.*",
                        "hint": "Use transition property: transition: property duration ease"
                    },
                    {
                        "id": "css_animations",
                        "title": "Create CSS Animations",
                        "description": "Use keyframes to create animations",
                        "points": 25,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*@keyframes.*{.*}.*animation\s*:.*",
                        "hint": "Use @keyframes and animation property"
                    },
                    {
                        "id": "css_transforms",
                        "title": "Apply CSS Transforms",
                        "description": "Use transform property for scaling, rotating, moving",
                        "points": 20,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*transform\s*:\s*(scale|rotate|translate).*",
                        "hint": "Use transform: scale(), rotate(), translate(), etc."
                    }
                ]
            },
            {
                "id": 9,
                "title": "JavaScript APIs",
                "description": "Work with browser APIs and async programming",
                "tasks": [
                    {
                        "id": "js_fetch_api",
                        "title": "Use Fetch API",
                        "description": "Make HTTP requests using the Fetch API",
                        "points": 30,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*fetch\s*\(.*\).*\.then.*",
                        "hint": "Use fetch() to make HTTP requests and handle with .then()"
                    },
                    {
                        "id": "js_async_await",
                        "title": "Use Async/Await",
                        "description": "Handle asynchronous operations with async/await",
                        "points": 25,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*async\s+function.*await.*",
                        "hint": "Use async functions and await keyword for promises"
                    },
                    {
                        "id": "js_local_storage",
                        "title": "Use Local Storage",
                        "description": "Store and retrieve data using localStorage",
                        "points": 20,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*(localStorage\.setItem|localStorage\.getItem).*",
                        "hint": "Use localStorage.setItem() and localStorage.getItem()"
                    }
                ]
            },
            {
                "id": 10,
                "title": "Web Project",
                "description": "Build a complete web application",
                "tasks": [
                    {
                        "id": "project_structure",
                        "title": "Create Project Structure",
                        "description": "Organize files in a proper project structure",
                        "points": 15,
                        "file_pattern": r".*(index\.html|style\.css|script\.js)$",
                        "validation_regex": r".*",
                        "hint": "Create index.html, style.css, and script.js files"
                    },
                    {
                        "id": "project_functionality",
                        "title": "Add Interactive Features",
                        "description": "Combine HTML, CSS, and JavaScript for a working app",
                        "points": 35,
                        "file_pattern": r".*\.js$",
                        "validation_regex": r".*addEventListener.*querySelector.*",
                        "hint": "Create an interactive app using DOM manipulation and event handling"
                    },
                    {
                        "id": "project_styling",
                        "title": "Apply Professional Styling",
                        "description": "Use advanced CSS for professional appearance",
                        "points": 25,
                        "file_pattern": r".*\.css$",
                        "validation_regex": r".*(flexbox|grid|transition|media).*",
                        "hint": "Use modern CSS techniques: flexbox/grid, transitions, responsive design"
                    }
                ]
            }
        ]
    
    def _load_progress(self):
        """Load progress from file"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    data = json.load(f)
                    self.current_lesson = data.get('current_lesson', 0)
                    self.completed_tasks = set(data.get('completed_tasks', []))
                    self.score = data.get('score', 0)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
    
    def _save_progress(self):
        """Save progress to file"""
        data = {
            'current_lesson': self.current_lesson,
            'completed_tasks': list(self.completed_tasks),
            'score': self.score
        }
        with open(self.progress_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def show_lessons(self):
        """Display available lessons"""
        print("\n📚 Available Lessons:")
        print("=" * 50)
        for i, lesson in enumerate(self.lessons):
            status = "✅" if i < self.current_lesson else "🔒" if i > self.current_lesson else "📖"
            print(f"{status} {lesson['id']}. {lesson['title']}")
            print(f"   {lesson['description']}")
            if i == self.current_lesson:
                print("   ← Current lesson")
            print()
    
    def show_current_lesson(self):
        """Display current lesson details"""
        if self.current_lesson >= len(self.lessons):
            print("🎉 Congratulations! You've completed all lessons!")
            return
        
        lesson = self.lessons[self.current_lesson]
        print(f"\n📖 Lesson {lesson['id']}: {lesson['title']}")
        print("=" * 50)
        print(f"Description: {lesson['description']}")
        print("\n📝 Tasks:")
        
        for task in lesson['tasks']:
            status = "✅" if task['id'] in self.completed_tasks else "⏳"
            print(f"  {status} {task['title']} ({task['points']} points)")
            print(f"     {task['description']}")
            if task['id'] not in self.completed_tasks:
                print(f"     💡 Hint: {task['hint']}")
            print()
    
    def verify_task(self, task_id: str) -> bool:
        """Verify if a task is completed correctly"""
        current_lesson = self.lessons[self.current_lesson] if self.current_lesson < len(self.lessons) else None
        if not current_lesson:
            print("❌ No current lesson available")
            return False
        
        task = None
        for t in current_lesson['tasks']:
            if t['id'] == task_id:
                task = t
                break
        
        if not task:
            print(f"❌ Task '{task_id}' not found in current lesson")
            return False
        
        if task_id in self.completed_tasks:
            print(f"✅ Task '{task['title']}' already completed!")
            return True
        
        # Look for files matching the pattern
        files_found = []
        for file in os.listdir('.'):
            if re.match(task['file_pattern'], file):
                files_found.append(file)
        
        if not files_found:
            print(f"❌ No files found matching pattern: {task['file_pattern']}")
            print(f"💡 Hint: {task['hint']}")
            return False
        
        # Validate file contents
        for file in files_found:
            try:
                with open(file, 'r') as f:
                    content = f.read()
                    if re.search(task['validation_regex'], content, re.DOTALL | re.IGNORECASE):
                        print(f"✅ Task '{task['title']}' completed successfully!")
                        print(f"📁 Verified file: {file}")
                        self.completed_tasks.add(task_id)
                        self.score += task['points']
                        self._save_progress()
                        
                        # Check if all tasks in lesson are complete
                        lesson_tasks = {t['id'] for t in current_lesson['tasks']}
                        if lesson_tasks.issubset(self.completed_tasks):
                            print(f"🎉 Lesson {current_lesson['id']} completed!")
                            self.current_lesson += 1
                            self._save_progress()
                        
                        return True
            except FileNotFoundError:
                continue
        
        print(f"❌ Task validation failed. Make sure your code matches the requirements.")
        print(f"💡 Hint: {task['hint']}")
        return False
    
    def show_progress(self):
        """Show current progress"""
        total_tasks = sum(len(lesson['tasks']) for lesson in self.lessons)
        completed_count = len(self.completed_tasks)
        
        print(f"\n📊 Your Progress:")
        print("=" * 30)
        print(f"Score: {self.score} points")
        print(f"Tasks completed: {completed_count}/{total_tasks}")
        print(f"Current lesson: {self.current_lesson + 1}/{len(self.lessons)}")
        
        if completed_count > 0:
            percentage = (completed_count / total_tasks) * 100
            bar_length = 20
            filled_length = int(percentage * bar_length // 100)
            bar = "█" * filled_length + "░" * (bar_length - filled_length)
            print(f"Progress: [{bar}] {percentage:.1f}%")
    
    def reset_progress(self):
        """Reset all progress"""
        self.current_lesson = 0
        self.completed_tasks = set()
        self.score = 0
        if os.path.exists(self.progress_file):
            os.remove(self.progress_file)
        print("🔄 Progress reset successfully!")


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(description="Interactive Web Development Learning Tool")
    parser.add_argument('command', nargs='?', choices=['lessons', 'current', 'verify', 'progress', 'reset', 'help'], 
                       default='help', help='Command to execute')
    parser.add_argument('--task', '-t', help='Task ID to verify')
    
    args = parser.parse_args()
    course = Course()
    
    print("🌐 Welcome to learn-web!")
    print("An interactive course to teach you web development basics\n")
    
    if args.command == 'lessons':
        course.show_lessons()
    elif args.command == 'current':
        course.show_current_lesson()
    elif args.command == 'verify':
        if not args.task:
            print("❌ Please specify a task ID with --task or -t")
            print("💡 Use 'python learn_web.py current' to see available tasks")
        else:
            course.verify_task(args.task)
    elif args.command == 'progress':
        course.show_progress()
    elif args.command == 'reset':
        course.reset_progress()
    else:  # help
        print("Available commands:")
        print("  lessons  - Show all available lessons")
        print("  current  - Show current lesson and tasks")
        print("  verify   - Verify a completed task (use with --task <task_id>)")
        print("  progress - Show your learning progress")
        print("  reset    - Reset all progress")
        print("  help     - Show this help message")
        print("\nExample usage:")
        print("  python learn_web.py lessons")
        print("  python learn_web.py current")
        print("  python learn_web.py verify --task html_basic_structure")


if __name__ == "__main__":
    main()