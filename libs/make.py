import sys
import markmin2html

FRAME = """<!doctype html>  
<html lang="en">
  
  <head>
    <meta charset="utf-8">
    <title>Massimo Di Pierro</title>    
    <meta name="description" content="">
    <meta name="author" content="Massimo Di Pierro">    
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <link rel="stylesheet" href="{{=reveal}}/css/reset.css" type="text/css">
    <link rel="stylesheet" href="{{=reveal}}/css/main.css" type="text/css">
    <link rel="stylesheet" href="{{=reveal}}/css/print.css" type="text/css" media="print">
    <link rel="stylesheet" href="{{=reveal}}/lib/zenburn.css" type="text/css">
  </head>
  
  <body>
    
    <div id="reveal">
      
      <!-- Used to fade in a background when a specific slide state is reached -->
      <div class="state-background"></div>
      
      <!-- Any section element inside of this container is displayed as a slide -->
      <div class="slides">

	{{include}}

      </div>
      
      <!-- The navigational controls UI -->
      <aside class="controls">
	<a class="left" href="#">&#x25C4;</a>
	<a class="right" href="#">&#x25BA;</a>
	<a class="up" href="#">&#x25B2;</a>
	<a class="down" href="#">&#x25BC;</a>
      </aside>
      
      <!-- Displays presentation progress, max value changes via JS to reflect # of slides -->
      <div class="progress"><span></span></div>
      
    </div>
    
    <script src="{{=reveal}}/js/reveal.js"></script>
    <script src="{{=mathjax}}/MathJax.js?config=default"></script>
    
    <!-- Optional libraries for code syntax highlighting and classList support in IE9 -->
    <script src="{{=reveal}}/lib/highlight.js"></script>
    <script src="{{=reveal}}/lib/classList.js"></script>
    
    <script>
      // Parse the query string into a key/value object
      var query = {};
      location.search.replace( /[A-Z0-9]+?=(\w*)/gi, function(a) {
        query[ a.split( '=' ).shift() ] = a.split( '=' ).pop();
      } );

      // Fires when a slide with data-state=customevent is activated
      Reveal.addEventListener( 'customevent', function() {
        alert( '"customevent" has fired' );
      } );

      // Fires each time a new slide is activated
      Reveal.addEventListener( 'slidechanged', function( event ) {
        // event.indexh & event.indexv
      } );

      Reveal.initialize({
        // Display controls in the bottom right corner
        controls: true,
      
        // Display a presentation progress bar
        progress: true,

        // If true; each slide will be pushed to the browser history
        history: true,
      
        // Loops the presentation, defaults to false
        loop: false,

        // Flags if mouse wheel navigation should be enabled
        mouseWheel: true,

        // Apply a 3D roll to links on hover
        rollingLinks: true,

        // UI style
        theme: query.theme || 'default', // default/neon

        // Transition style
        transition: query.transition || 'default' // default/cube/page/concave/linear(2d)
      });
      
      hljs.initHighlightingOnLoad();
    </script>
  </body>
</html>
"""

def make(text,local=False):    
    html = markmin2html.markmin2html(text,extra=dict(html=lambda html:html))
    html = html.replace('<h1>','</section><section><h1>')
    html = html.replace('<h2>','</section><section><h2>')
    html = html.strip()[10:]+'</section>'
    frame = FRAME
    if local:
        frame = frame.replace('{{=reveal}}','reveal')
        frame = frame.replace('{{=mathjax}}','mathjax')
    else:
        frame = frame.replace('{{=reveal}}','http://lab.hakim.se/reveal-js')
        frame = frame.replace('{{=mathjax}}','http://cdn.mathjax.org/mathjax/latest')        
    return frame.replace('{{include}}',html)

if __name__=='__main__':
    print make(open(sys.argv[1]).read())
