import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch, MagicMock, call

# Import the components we want to test
from commands.registry import execute_command, get_commands_json
from brain.assistant import classify_intent
from main import jarvis_callback

class TestCommandExecution(unittest.TestCase):
    
    def test_execute_youtube_command(self):
        """Test that YouTube command executes correctly"""
        with patch('webbrowser.open') as mock_open:
            result = execute_command('open_youtube')
            mock_open.assert_called_once_with('https://www.youtube.com')
            self.assertEqual(result, 'Otwieram YouTube...')
    
    def test_execute_show_commands(self):
        """Test that show_commands executes correctly"""
        with patch('subprocess.Popen') as mock_popen, \
             patch('tempfile.NamedTemporaryFile') as mock_temp_file:
            
            # Setup the mock for the temp file
            mock_file = MagicMock()
            mock_file.name = 'temp_test_file.txt'
            mock_temp_file.return_value.__enter__.return_value = mock_file
            
            result = execute_command('show_commands')
            
            # Check that the temp file was written to
            mock_file.write.assert_called()
            # Check that notepad was opened with the temp file
            mock_popen.assert_called_once()
            self.assertEqual(result, 'Wyświetlam listę komend w Notatniku.')
    
    def test_execute_nonexistent_command(self):
        """Test handling of non-existent commands"""
        result = execute_command('nonexistent_command')
        self.assertIsNone(result)
    
    def test_get_commands_json(self):
        """Test that commands are correctly serialized to JSON"""
        json_str = get_commands_json()
        self.assertIn('"name": "open_youtube"', json_str)
        self.assertIn('"name": "show_commands"', json_str)

class TestAssistantBrain(unittest.TestCase):
    
    @patch('openai.OpenAI')
    def test_classify_intent_command(self, mock_openai):
        """Test intent classification for a command"""
        # Setup the mock OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "COMMAND: open_youtube"
        mock_client.chat.completions.create.return_value = mock_response
        
        intent, data = classify_intent("Otwórz YouTube")
        
        self.assertEqual(intent, "COMMAND")
        self.assertEqual(data, "open_youtube")
    

class TestJarvisCallback(unittest.TestCase):
    
    @patch('main.speak')
    @patch('main.save_last_audio')
    @patch('main.transcribe')
    @patch('main.classify_intent')
    @patch('main.execute_command')
    def test_jarvis_callback_command_success(self, mock_execute, mock_classify, 
                                            mock_transcribe, mock_save, mock_speak):
        """Test Jarvis callback with a successful command execution"""
        # Setup mocks
        mock_transcribe.return_value = "otwórz YouTube"
        mock_classify.return_value = ("COMMAND", "open_youtube")
        mock_execute.return_value = "Otwieram YouTube..."
        
        # Call the function
        jarvis_callback()
        
        # Verify the expected flow
        mock_speak.assert_has_calls([
            call("Słucham?"),
            call("Otwieram YouTube...")
        ])
        mock_save.assert_called_once()
        mock_transcribe.assert_called_once()
        mock_classify.assert_called_once_with("otwórz YouTube")
        mock_execute.assert_called_once_with("open_youtube")
    
    @patch('main.speak')
    @patch('main.save_last_audio')
    @patch('main.transcribe')
    @patch('main.classify_intent')
    @patch('main.execute_command')
    def test_jarvis_callback_command_failure(self, mock_execute, mock_classify, 
                                            mock_transcribe, mock_save, mock_speak):
        """Test Jarvis callback with a failed command execution"""
        # Setup mocks
        mock_transcribe.return_value = "wykonaj nieistniejącą komendę"
        mock_classify.return_value = ("COMMAND", "nonexistent_command")
        mock_execute.return_value = None  # Command not found
        
        # Call the function
        jarvis_callback()
        
        # Verify the expected flow
        mock_speak.assert_has_calls([
            call("Słucham?"),
            call("Nie rozumiem tej komendy.")
        ])
    
    @patch('main.speak')
    @patch('main.save_last_audio')
    @patch('main.transcribe')
    @patch('main.classify_intent')
    @patch('main.execute_command')
    def test_jarvis_callback_chat(self, mock_execute, mock_classify, 
                                mock_transcribe, mock_save, mock_speak):
        """Test Jarvis callback with a chat response"""
        # Setup mocks
        mock_transcribe.return_value = "jak się masz?"
        mock_classify.return_value = ("CHAT", "Mam się dobrze, dziękuję za pytanie!")
        
        # Call the function
        jarvis_callback()
        
        # Verify the expected flow
        mock_speak.assert_has_calls([
            call("Słucham?"),
            call("Mam się dobrze, dziękuję za pytanie!")
        ])
        mock_execute.assert_not_called()
    
    @patch('main.speak')
    @patch('main.save_last_audio')
    @patch('main.transcribe')
    @patch('main.classify_intent')
    @patch('main.execute_command')
    def test_jarvis_callback_unknown(self, mock_execute, mock_classify, 
                                    mock_transcribe, mock_save, mock_speak):
        """Test Jarvis callback with an unknown intent"""
        # Setup mocks
        mock_transcribe.return_value = "niezrozumiały tekst"
        mock_classify.return_value = ("UNKNOWN", "Nie rozumiem")
        
        # Call the function
        jarvis_callback()
        
        # Verify the expected flow
        mock_speak.assert_has_calls([
            call("Słucham?"),
            call("Nie jestem pewien, jak odpowiedzieć.")
        ])
        mock_execute.assert_not_called()

if __name__ == '__main__':
    unittest.main()