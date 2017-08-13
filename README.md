# 'preprocessing'

Text pre-processing package to aid in NLP package development for Python3. With this package you can order text cleaning functions in the order you prefer rather than relying on the order of an arbitrary NLP package.

# Installation

pip:
~~~~
pip install preprocessing
~~~~

PyPI:
You can also download the source distribution from:

> [https://pypi.python.org/pypi/preprocessing/](https://pypi.python.org/pypi/preprocessing/)

You can then perform:
~~~~
pip install <path_to_tar_file>
~~~~
on the tar file, or
~~~~
python setup.py install
~~~~
inside the extracted package to install *preprocessing*

# Example

Once you have the package installed, implementing it with Python3 takes the following form:

~~~~
import preprocessing
from preprocessing import keyword_tokenize, remove_non_bound_punct, remove_urls

text_string = "important string at: http://example.com"

clean_string = preprocessing.preprocess_text(text_string, [
    remove_urls,
    remove_non_bound_punct,
    keyword_tokenize
])

print(clean_string)
~~~~
> out: "important string"

Should the functions be performed in a different order (i.e. keyword_tokenize - remove_urls - remove_non_bound_punct) :

> out: "important string http example.com"

# Organisation

This package is comprised of a single module with no intended subpackages currently. The 'preprocessing' package is dependent on NLTK for tokenizers and stopwords. However, ignoring this, the package only has built-in dependencies from Python 3.

#Contributing

If you feel like contributing:

* [Check for open issues](https://github.com/mwtmurphy/pre-processing/issues) or open a new issue.
* Fork the preprocessing repository to start making your changes
* Write a test which shows the bug was fixed or that the feature works as expected
* Send a pull request and remember to add yourself to CONTRIBUTORS.txt

# License

This project is licensed under the MIT license (see LICENSE file)