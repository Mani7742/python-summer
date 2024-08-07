# First of All we have to install pywhatkit
# For installation of pywhatkit we hace to run this command in our terminal
# pip install pywhatkit
# For verfication of pywhatkit we have to run this command
# python -c "import pywhatkit; print(pywhatkit.__version__)"
import pywhatkit as pw
txt = """Python has become the de facto language for data science and machine learning.
Libraries like NumPy, Pandas, and Matplotlib simplify data manipulation, analysis, and visualization.
Moreover, Python's role in machine learning and artificial intelligence is unparalleled."""
# pw.text_to_handwriting(txt,"Demo.png",[0,0,138])
pw.text_to_handwriting(txt)
print("End")