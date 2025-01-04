import unittest
from unittest.mock import patch, Mock
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import requests

# Import the function to be tested
from weather import weather_data, Time  # Replace 'your_module' with your actual module name

class TestWeatherApp(unittest.TestCase):

    pass
    @patch('requests.get')
    def test_weather_data_success(self, mock_get):
        # Mock the requests.get method
        mock_response = Mock()
        mock_response.json.return_value = {
            'weather': [{'description': 'clear sky', 'icon': '01d'}],
            'main': {'temp': 285.15, 'temp_max': 290.15, 'temp_min': 280.15, 'humidity': 50},
            'wind': {'speed': 3.5}
        }
        mock_get.return_value = mock_response

        # Mock the Time function
        # mock_time = Mock(return_value=('Monday', ['2024-07-15'], ['12:00:00']))
        # datetime.datetime.now = mock_time

        # Set up tkinter components
        window = tkinter.Tk()
        textfilde = tkinter.Entry(window)
        label1 = tkinter.Label(window)
        image = tkinter.Label(window)
        label2 = tkinter.Label(window)
        label = tkinter.Label(window)
        
        # Call the function with mock data
        textfilde.insert(0, 'London')
        weather_data()
        
        # Check if tkinter components are updated correctly
        self.assertEqual(label1.cget('text'), 'clear sky\n12°C')
        self.assertEqual(label2.cget('text'), '\nMax_temp: 17         Min_temp: 7\nHumidity: 50         Wind: 3.5')
        self.assertEqual(label.cget('text'), 'Monday  2024-07-15  12:00:00')

    @patch('requests.get')
    def test_weather_data_failure(self, mock_get):
        # Mock the requests.get method to simulate failure
        mock_response = Mock()
        mock_response.json.side_effect = Exception('City not found')
        mock_get.return_value = mock_response

        # Set up tkinter components
        window = tkinter.Tk()
        textfilde = tkinter.Entry(window)
        
        # Call the function with mock data
        textfilde.insert(0, 'UnknownCity')
        with self.assertRaises(messagebox.showerror):
            weather_data()

if __name__ == '__main__':
    unittest.main()
