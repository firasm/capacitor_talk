# Import libraries

global pd,np,plt#,IFrame

pd = __import__('pandas',globals(),locals())
np = __import__('numpy', globals(),locals())
plt = __import__('matplotlib.pyplot', globals(),locals(),['plt'])
#IFrame = __import__('IPython.display', globals(),locals(), ['IFrame'])

from IPython.display import IFrame

# Jupyter Notebooks
    
from vega_datasets import data
mtcars = data.cars()

## Links

stud_finder = 'https://www.youtube.com/embed/rzYkyBsYXA0?start=42'
capacitor_phet = 'https://phet.colorado.edu/sims/html/capacitor-lab-basics/latest/capacitor-lab-basics_en.html'

## RISE template

from traitlets.config.manager import BaseJSONConfigManager
from pathlib import Path
path = Path.home() / ".jupyter" / "nbconfig"
cm = BaseJSONConfigManager(config_dir=str(path))
tmp = cm.update(
        "rise",
        {
            "theme": "simple", # https://revealjs.com/themes/
            "transition": "fade",
            "start_slideshow_at": "selected",
            "autolaunch": False,
            "width": "100%",
            "height": "100%",
            "header": "",
            "footer":"",
            "scroll": True,
            "enable_chalkboard": True,
            "slideNumber": True,
            "center": False,
            "controlsLayout": "edges",
            "slideNumber": True,
            "hash": True,
        }
    )

## Conceptual questions at the end

import ipywidgets as widgets
from IPython.display import display
from IPython.display import clear_output

## Full Credit to this GH issue: https://github.com/jupyter-widgets/ipywidgets/issues/2487

def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    # Bizarre ASCI colour codes here: https://tforgione.fr/posts/ansi-escape-codes/

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;0;42m' + " Right! You got it! " + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Incorrect, try again! " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return

    check = widgets.Button(description="submit")
    check.on_click(check_selection)

    return widgets.VBox([description_out, alternativ, check, feedback_out])
    
Q1 = create_multipleChoice_widget('CQ 1 - Does the capacitance of a device depend on the applied voltage?',['apple','banana','pear'],'pear')
Q2 = create_multipleChoice_widget('CQ 2 - Would you place the plates of a parallel-plate capacitor closer together or farther apart to increase their capacitance?',['cat','dog','mouse'],'dog')
Q3 = create_multipleChoice_widget('CQ 3 - The value of the capacitance is zero if the plates are not charged. True or False?',['True', 'False'],'True')
Q4 = create_multipleChoice_widget('CQ 4 - Why does adding a dielectric increase the capacitance?',['True', 'False'],'True')
Q5 = create_multipleChoice_widget('CQ 5 - What would happen if a conducting slab rather than a dielectric were inserted into the gap between the capacitor plates.',['Option A', 'Option B', 'Option C', 'Option D'],'Option C')