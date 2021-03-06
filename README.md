# SciPy project

![](images/SeasonofDocs_Logo_SecondaryGrey_300ppi.png)


## User survey

Our SciPy user survey has been closed: consult the full report [here](https://github.com/mkg33/GSoD/blob/master/user_survey_summary.pdf).

## Graphical guides

This repository contains the suggested graphical guides to be included in the SciPy documentation. The premise of the guides is to facilitate the navigation and exploration of the documentation. **All comments welcome.**

* I intend to use the typographical and graphical conventions presented in the file called [`hierarchy.tex`](API/hierarchy.tex)
* the linear algebra file ([`sample_guide.tex`](tutorials/sample_guide.tex)) was the first prototype for this project and the code is still a bit messy
* the SciPy official colour scheme was used in the two guides - this is sill subject to change; i.e., accessibility issues, saturation, etc.
* the three [screenshots](images) present different colour saturation - if you wish, you can compare them and express your opinion
* I also have several other prototypes but they look pretty much the same as [`hierarchy.tex`](API/hierarchy.txt), so I won't be posting them for now

### Additional details and updates

* the motivation behind breaking the line and placing the ampersand at the beginning of the line is given, e.g., [here](https://graphicdesign.stackexchange.com/questions/15783/is-ampersand-allowed-at-the-beginning-of-line)
* see also this related issue [#10875](https://github.com/scipy/scipy/issues/10875)
* based on the above issue, I'll now be redesigning the current prototype and I'll use WBS diagrams instead


Here is a prototype:

![sample](https://user-images.githubusercontent.com/26354268/65713823-4c3a8600-e09a-11e9-921d-4db6cfa729fd.jpg)

And here, the current WBS version:

![WBS](API/hierarchy_WBS.jpg)

![linalg](tutorials/linalg.jpg)


## Revision of the current documentation

I'm also working on correcting typos, stylistic inconsistencies, grammar, punctuation, etc., in the current documentation.

Consult the related pull requests for more details:

* [#10823](https://github.com/scipy/scipy/pull/10823)
* [#10800](https://github.com/scipy/scipy/pull/10800)
* [#11067](https://github.com/scipy/scipy/pull/11067)

---
:octocat: *the project has now been completed*
