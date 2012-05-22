# title

### author

## Overview

- Make a file ``test.mm`` using markmin syntax explained below.
- Run: ``libs/make.py test.mm > test.html``
- open ``test.html``

## Syntax example

``
**bold**
''italic''
-----
quote
-----
[[link http://google.com]]
``

renders as 

**bold**
''italic''
-----
quote
-----
[[link http://google.com]]

## Embedding images

``
[[image http://bit.ly/KYqon8 center 200px]]
``

renders as

[[image http://bit.ly/KYqon8 center 200px]]

## Embedding code

``
!`!!`!
def index():
    print 'hello world'
!`!!`!
``

renders as

``
def index():
    print 'hello world'
``

## Embedding Latex Formulas

``
\[ \int_a^b sin(x) dx \]
``

renders as 

\[ \int_a^b sin(x) dx \]

Use ``\(...\)`` for inline formulas.

## Embedding videos

``
!`!!`!<iframe src="http://player.vimeo.com/video/25242353" width="400" height="250" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>!`!!`!:html
``

renders as 

``<iframe src="http://player.vimeo.com/video/25242353" width="400" height="250" frameborder="0" webkitA\
llowFullScreen mozallowfullscreen allowFullScreen></iframe>``:html

## Embedding a table

``
---------
X | 0 | 0
0 | X | 0
0 | 0 | X
---------
``

renders as:

---------
X | 0 | 0
0 | X | 0
0 | 0 |	X
---------
