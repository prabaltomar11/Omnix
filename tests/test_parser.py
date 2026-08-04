from utils.parser import extract_command

def test_open_command():
    result = extract_command("open spotify")
    assert result == ("open", "spotify", "spotify")