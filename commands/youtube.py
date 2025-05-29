import webbrowser

class OpenYouTubeCommand:
    name = "open_youtube"
    description="Otwiera stronę YouTube w przeglądarce."

    def execute(self, argument: str = ""):
        webbrowser.open("https://www.youtube.com")
        return "Otwieram YouTube..."