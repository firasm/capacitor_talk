# Import libraries

import seaborn as sns
sns.set('talk', font_scale=1.4)
sns.set_style('whitegrid')

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
    
Q1 = create_multipleChoice_widget('CQ 1 - Does the capacitance of a device depend on the applied voltage?',['Yes','No'],'No')
Q2 = create_multipleChoice_widget('CQ 2 - Would you place the plates of a parallel-plate capacitor closer together or farther apart to increase their capacitance?',['Closer together','Further apart'],'Further apart')
Q3 = create_multipleChoice_widget('CQ 3 - The value of the capacitance is zero if the plates are not charged. True or False?',['True', 'False'],'True')
Q4 = create_multipleChoice_widget('CQ 4 - Why does adding a dielectric increase the capacitance?',['Additional surface area to store charge',
                                                                                                   'E field increases', 
                                                                                                   'E field decreases',],'E field decreases')
Q5 = create_multipleChoice_widget('CQ 5 - What would happen if a conducting slab rather than a dielectric was inserted between the capacitor plates, without touching? (Bonus: why?)',['Capacitance would increase', 'Capacitance would decrease', 'Energy stored will be released', 'Circuit would break'],'Capacitance would increase')



## Markdown in python cells

from IPython.display import Markdown


## hide code

def hide_code_in_slideshow():   
    from IPython import display
    import binascii
    import os
    uid = binascii.hexlify(os.urandom(8)).decode()    
    html = """<div id="%s"></div>
    <script type="text/javascript">
        $(function(){
            var p = $("#%s");
            if (p.length==0) return;
            while (!p.hasClass("cell")) {
                p=p.parent();
                if (p.prop("tagName") =="body") return;
            }
            var cell = p;
            cell.find(".input").addClass("hide-in-slideshow")
        });
    </script>""" % (uid, uid)

    # Run this in a cell
    # display.display_html(html, raw=True)

## Cute thing to show the slides are interactive

def ready():
    print("Ready to start!")

# Jupyterthemes command
#!jt -t grade3 -tfs 14 -dfs 14 -ofs 14 -T

## Plotting functions

def plot_VQ(voltage,charge):
    
    VQ = {'Voltage': voltage,
          'Charge': charge}

    VQ = pd.DataFrame(VQ)

    ax = sns.scatterplot(x='Voltage',y='Charge', data=VQ)
    sns.despine()

    ax = ax.set(xlabel = 'Voltage ($V$)',
           ylabel = 'Charge ($pC$)',
           ylim = (0, None),
           xlim = (0,None),
           title = 'Parallel Plate Capacitor: $Q$ and $V$'
          )

def plot_dC(separation,capacitance):

    dC = {'Separation': separation,
          'Capacitance': capacitance}

    dC = pd.DataFrame(dC)

    ax = sns.scatterplot(x='Separation',y='Capacitance', data=dC)
    sns.despine()
    ax = ax.set(xlabel = 'Separation ($mm$)',
           ylabel = 'Capacitance ($pF$)',
           ylim = (0, max(capacitance)*1.25),
           xlim = (0,max(separation)*1.2),
           title = 'Parallel Plate Capacitor: $C$ and $d$'
          )
    sns.set_style('whitegrid')

def plot_AC(area,capacitance):

    AC = {'Area': area,
          'Capacitance': capacitance}

    AC = pd.DataFrame(AC)

    ax = sns.scatterplot(x='Area',y='Capacitance', data=AC)
    sns.despine()
    ax = ax.set(xlabel = 'Area ($mm^2$)',
           ylabel = 'Capacitance ($pF$)',
           ylim = (0, None),
           xlim = (0,None),
           title = 'Parallel Plate Capacitor: $C$ and $A$'
          )
    sns.set_style('whitegrid')

