# Useful plugins and configurations

---

## Add a search bar
1. Add search support in `./docs/index.html` by adding following line before body's end
    ```html
    <html>
        //...
        <body>
            //... 
            <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
        </body>
    </html>
    ```
   
1. Also add this line in `window.$docsify` script
    ```html
    <script>
        window.$docsify = {
            //...
            search: 'auto',
            //...           
        }
    </script>
    ```
   
> :bangbang: Search index has a `maxAge` default value of one day, so you need to clear localStorage in dev tool to redo the indexation, or reduce its value


## Add ability to copy code snippets
Simply add this line before body's end
```html
<html>
    //...
    <body>
        //...
        <script src="//cdn.jsdelivr.net/npm/docsify-copy-code"></script>
    </body>
</html>
```


## Add Mermaid Diagram support
1. Add those lines in HTML Header on top of file
    ```html
    <head>
        //...
        <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.css">
        <script src="//cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    </head>
    ```
    
1. Also, you need to parse mermaid .md in a different way, for this add this code snippet in `window.$docsify` script
    ```html
    <script>
        window.$docsify = {
            //...
            markdown: {
                renderer: {
                    code: function (code, lang) {
                        if (lang === "mermaid") {
                            return (
                                '<div class="mermaid">' + mermaid.render('mermaid-svg-' + num++, code) + "</div>"
                            );
                        }
                        return this.origin.code.apply(this, arguments);
                    }
                }
            },
            //...           
        }
    </script>
    ```
    
1. Finally, add those two lines below `window.$docsify`
    ```html
    <script>
        window.$docsify = {
            //...           
        }
        let num = 0;
        mermaid.initialize({startOnLoad: false});
    </script>
    ```