import webbrowser

class OpenYouTubeCommand:
    name = "open_youtube"

    def execute(self, argument: str = ""):
        webbrowser.open("https://www.youtube.com")
        return "Otwieram YouTube..."