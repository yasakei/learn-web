#!/usr/bin/env python3
"""
Tests for the learn-web CLI tool
"""

import os
import tempfile
import shutil
import json
import unittest
from learn_web import Course


class TestLearnWeb(unittest.TestCase):
    """Test cases for the learn-web tool"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
        self.course = Course()
    
    def tearDown(self):
        """Clean up test environment"""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)
    
    def test_initial_state(self):
        """Test initial course state"""
        self.assertEqual(self.course.current_lesson, 0)
        self.assertEqual(len(self.course.completed_tasks), 0)
        self.assertEqual(self.course.score, 0)
    
    def test_lesson_structure(self):
        """Test that lessons are properly structured"""
        self.assertEqual(len(self.course.lessons), 10)
        self.assertEqual(self.course.lessons[0]['title'], "HTML Basics")
        self.assertEqual(self.course.lessons[1]['title'], "CSS Styling")
        self.assertEqual(self.course.lessons[2]['title'], "JavaScript Basics")
        self.assertEqual(self.course.lessons[3]['title'], "HTML Forms")
        self.assertEqual(self.course.lessons[4]['title'], "CSS Layout")
    
    def test_html_task_verification(self):
        """Test HTML task verification"""
        # Create a valid HTML file
        with open('test.html', 'w') as f:
            f.write('<html><head></head><body></body></html>')
        
        result = self.course.verify_task('html_basic_structure')
        self.assertTrue(result)
        self.assertIn('html_basic_structure', self.course.completed_tasks)
        self.assertEqual(self.course.score, 10)
    
    def test_css_task_verification(self):
        """Test CSS task verification"""
        # Move to lesson 2 first
        self.course.current_lesson = 1
        
        # Create a valid CSS file
        with open('test.css', 'w') as f:
            f.write('body { color: red; }')
        
        result = self.course.verify_task('css_basic_styling')
        self.assertTrue(result)
        self.assertIn('css_basic_styling', self.course.completed_tasks)
        self.assertEqual(self.course.score, 15)
    
    def test_js_task_verification(self):
        """Test JavaScript task verification"""
        # Move to lesson 3 first
        self.course.current_lesson = 2
        
        # Create a valid JS file
        with open('test.js', 'w') as f:
            f.write('function myFunction() { console.log("Hello"); }')
        
        result = self.course.verify_task('js_basic_script')
        self.assertTrue(result)
        self.assertIn('js_basic_script', self.course.completed_tasks)
        self.assertEqual(self.course.score, 20)
    
    def test_invalid_task_verification(self):
        """Test verification of invalid tasks"""
        result = self.course.verify_task('nonexistent_task')
        self.assertFalse(result)
    
    def test_progress_persistence(self):
        """Test that progress is saved and loaded correctly"""
        # Complete all HTML tasks to advance lesson
        with open('test.html', 'w') as f:
            f.write('<html><head></head><body></body></html>')
        self.course.verify_task('html_basic_structure')
        
        with open('test2.html', 'w') as f:
            f.write('<html><head></head><body><header></header><main></main><footer></footer></body></html>')
        self.course.verify_task('html_semantic_elements')
        
        with open('test3.html', 'w') as f:
            f.write('<html><head></head><body><h1>Title</h1><p>Text</p><ul><li>Item</li></ul><a href="#">Link</a></body></html>')
        self.course.verify_task('html_content_elements')
        
        # Create new course instance (simulates restart)
        new_course = Course()
        self.assertEqual(new_course.current_lesson, 1)  # Should advance to lesson 2
        self.assertIn('html_basic_structure', new_course.completed_tasks)
        self.assertIn('html_semantic_elements', new_course.completed_tasks)
        self.assertIn('html_content_elements', new_course.completed_tasks)
        self.assertEqual(new_course.score, 35)  # 10 + 15 + 10
    
    def test_lesson_progression(self):
        """Test that lessons progress correctly when tasks are completed"""
        # Complete only first HTML task - lesson should not advance yet
        with open('test.html', 'w') as f:
            f.write('<html><head></head><body></body></html>')
        self.course.verify_task('html_basic_structure')
        self.assertEqual(self.course.current_lesson, 0)  # Should still be on lesson 1
        
        # Complete all HTML tasks to advance to next lesson
        with open('test2.html', 'w') as f:
            f.write('<html><head></head><body><header></header><main></main><footer></footer></body></html>')
        self.course.verify_task('html_semantic_elements')
        
        with open('test3.html', 'w') as f:
            f.write('<html><head></head><body><h1>Title</h1><p>Text</p><ul><li>Item</li></ul><a href="#">Link</a></body></html>')
        self.course.verify_task('html_content_elements')
        
        self.assertEqual(self.course.current_lesson, 1)  # Should advance to CSS lesson
    
    def test_file_pattern_matching(self):
        """Test that file patterns work correctly"""
        # Test with wrong file extension
        with open('test.txt', 'w') as f:
            f.write('<html><head></head><body></body></html>')
        
        result = self.course.verify_task('html_basic_structure')
        self.assertFalse(result)  # Should fail because it's not an HTML file
    
    def test_content_validation(self):
        """Test that content validation works correctly"""
        # Create HTML file without proper structure
        with open('test.html', 'w') as f:
            f.write('<div>Just a div</div>')
        
        result = self.course.verify_task('html_basic_structure')
        self.assertFalse(result)  # Should fail validation
    
    def test_new_html_tasks(self):
        """Test new HTML tasks work correctly"""
        # Test semantic elements task
        with open('semantic.html', 'w') as f:
            f.write('<html><body><header>Header</header><main>Main</main><footer>Footer</footer></body></html>')
        
        result = self.course.verify_task('html_semantic_elements')
        self.assertTrue(result)
        self.assertIn('html_semantic_elements', self.course.completed_tasks)
        
        # Test content elements task  
        with open('content.html', 'w') as f:
            f.write('<html><body><h1>Title</h1><p>Text</p><ul><li>Item</li></ul><a href="#">Link</a></body></html>')
        
        result = self.course.verify_task('html_content_elements')
        self.assertTrue(result)
        self.assertIn('html_content_elements', self.course.completed_tasks)
    
    def test_new_css_tasks(self):
        """Test new CSS tasks work correctly"""
        # Move to CSS lesson
        self.course.current_lesson = 1
        
        # Test selectors and properties task
        with open('advanced.css', 'w') as f:
            f.write('.class { color: red; } #id { font-size: 16px; }')
        
        result = self.course.verify_task('css_selectors_properties')
        self.assertTrue(result)
        
        # Test box model task
        with open('boxmodel.css', 'w') as f:
            f.write('div { margin: 10px; padding: 5px; border: 1px solid black; }')
        
        result = self.course.verify_task('css_box_model')
        self.assertTrue(result)
    
    def test_new_js_tasks(self):
        """Test new JavaScript tasks work correctly"""
        # Move to JS lesson
        self.course.current_lesson = 2
        
        # Test variables and operators task
        with open('variables.js', 'w') as f:
            f.write('let x = 5; const y = 10; let result = x + y;')
        
        result = self.course.verify_task('js_variables_operators')
        self.assertTrue(result)
        
        # Test control structures task
        with open('control.js', 'w') as f:
            f.write('if (x > 0) { console.log("positive"); } for (let i = 0; i < 10; i++) { console.log(i); }')
        
        result = self.course.verify_task('js_control_structures')
        self.assertTrue(result)
    

if __name__ == '__main__':
    unittest.main()