import tempfile
import subprocess
from datetime import datetime

class ShowStatisticsCommand:
    name = "show_statistics"
    description = "Pokazuje statystyki użycia asystenta"
    category = "system"
    
    def __init__(self):
        self.usage_history = []
    
    def log_usage(self, command_name: str):
        """Dodaje wpis do historii użycia"""
        self.usage_history.append({
            'command': command_name,
            'timestamp': datetime.now(),
            'date': datetime.now().date()
        })
    
    def usage_generator(self):
        """Generator zwracający wpisy użycia"""
        for entry in self.usage_history:
            yield entry
    
    def daily_stats_generator(self):
        """Generator zwracający statystyki dzienne"""

        dates = list(set([entry['date'] for entry in self.usage_history]))
        
        for date in sorted(dates):
            daily_commands = [entry for entry in self.usage_history if entry['date'] == date]

            command_counts = {}
            for entry in daily_commands:
                cmd = entry['command']
                command_counts[cmd] = command_counts.get(cmd, 0) + 1
            
            yield {
                'date': date,
                'total_commands': len(daily_commands),
                'command_breakdown': command_counts,
                'most_used': max(command_counts.items(), key=lambda x: x[1]) if command_counts else None
            }
    
    def execute(self, argument: str = "", commands_list: list = []) -> str:
        report_lines = ["📊 Statystyki użycia Jarvis\n", "=" * 30, "\n"]
        
        total_usage = len(self.usage_history)
        unique_commands = len(set([entry['command'] for entry in self.usage_history]))
        
        report_lines.extend([
            f"Łączna liczba wykonanych komend: {total_usage}",
            f"Liczba różnych komend: {unique_commands}",
            "\n📈 Statystyki dzienne:\n"
        ])
        
        for daily_stat in self.daily_stats_generator():
            report_lines.append(f"📅 {daily_stat['date']}: {daily_stat['total_commands']} komend")
            if daily_stat['most_used']:
                report_lines.append(f"   Najczęściej używana: {daily_stat['most_used'][0]} ({daily_stat['most_used'][1]}x)")
            report_lines.append("")

        if self.usage_history:
            report_lines.extend([
                "\n🔍 Historia użycia:",
                *[f"• {entry['timestamp'].strftime('%H:%M:%S')} - {entry['command']}" 
                  for entry in list(self.usage_generator())[-10:]]  # Ostatnie 10 komend
            ])
        
        content = "\n".join(report_lines)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as f:
            f.write(content)
            temp_file_path = f.name
        
        subprocess.Popen(["notepad.exe", temp_file_path])
        return f"Wyświetlam statystyki użycia. Łącznie wykonano {total_usage} komend."