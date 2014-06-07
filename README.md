PETRARCH
========

Current development for the new Python Engine for Text Resolution And Related
Coding Hierarchy (PETRARCH) coder.

In a 
nutshell, this works -- it coded 60,000 AFP sentences from the GigaWord corpus without 
crashing, using the included dictionaries -- but the pattern matching is only partially 
implemented and the CAMEO dictionary still uses the old TABARI-style stemming which does 
not work in PATRARCH, which is to say there are a *lot* of patterns that no longer work. 
However, it now has almost all of the features of the TABARI coder.

Documentation could also use a little work (really??) but is fairly complete, though 
scattered in `"""..."""` blocks throughout the program.

##Installing

It is now possible to install the program. It is highly recommended that you
install within a virtual environment. This is alpha software, so things will
change moving forward. Seriously, install in a virtual environment.

To install (you're in a virtual environment, right?):

1) Clone the repo

  - For example, download the zip file into ``~/Downloads``.
  - This will put the repo into something like ``~/Downloads/petrarch``.

2) Run ``pip install -e ~/Downloads/petrarch``


This will install the program with a command-line hook. You can now run the program using:

``petrarch <COMMAND NAME> [OPTIONS]``

You can get more information using:

``petrarch -h``

**StanfordNLP:**

If you plan on using StanfordNLP for parsing within the program you will also
need to download that program. PETRARCH uses StanfordNLP 3.2.0, which can be
obtained from
[Stanford](http://www-nlp.stanford.edu/software/stanford-corenlp-full-2013-06-20.zip). 
PETRARCH's default configuration file assumes that this is unzipped and located
in the user's home directory in a directory named ``stanford-corenlp/``, e.g., ``~/stanford-corenlp``.

The program is stable enough that it is probably useable. The main thing that's
going to change are the underlying dictionaries and some organization of the
code. It's not *that* likely that there will be large changes in the API. 

##Running

Currently, you can run PETRARCH using the following command if installed:

``petrarch parse -i <INPUT FILE> -o <OUTPUT FILE>``

If not installed:

``python petrarch.py parse -i data/text/GigaWord.sample.PETR.xml -o test_output.txt``

There's also the option to specify a configuration file using the ``-c <CONFIG
FILE>`` flag, but the program will default to using ``PETR_config.ini``.

When you run the program, a ``PETRARCH.log`` file will be opened in the current
working directory. This file will contain general information, e.g., which
files are being opened, and error messages.

##Unit tests

Commits should always successfully complete

``petrarch validate``

This command defaults to the ``PETR.UnitTest.records.txt`` file included with the
program. Alternative files can be indicated using the ``-i`` option. For example
(this is equivalent to the default command):

``petrarch validate -i data/text/PETR.UnitTest.records.xml``

The final record should read

    Sentence: FINAL-RECORD [ DEMO ]
    ALL OF THE UNIT TESTS WERE CODED CORRECTLY. 
    No events should be coded
    No events were coded
    Events correctly coded in FINAL-RECORD
    Exiting: <Stop> record 

##Compatibilities with TABARI dictionaries

PETRARCH has a much richer dictionary syntax than TABARI, which will eventually accommodate 
the WordNet-enhanced dictionaries developed at Penn State as well as reducing the level 
of redundancy in the existing dictionaries. While the initial version of the program 
could use existing TABARI dictionaries, this compatibility will decline with further 
developments and only the PETRARCH-specific dictionaries can be used

15-Nov-2013: Requires TABARI 0.8 indented date restrictions, not older in-line format

23-Apr-2014: PETRARCH-formatted agents dictionary required

12-May-2014: Disjunctive phrases no longer recognized in the .verbs dictionary
