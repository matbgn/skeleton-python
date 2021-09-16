# Start documenting using docsify

---

## Install docsify and init `./docs` folder from scratch
1. Init npm repo and install docsify-cli or do it globally
    ```javascript
      npm init
      npm i -D docsify-cli
    
    OR
    
      npm i docsify-cli -g
    ```

1. Init docs folder
    ```javascript
    npx docsify init ./docs
    ```
   
1. Serve documentation locally
   ```javascript
   npx docsify serve docs
   ```

## Install docsify and init `./docs` by cloning this repo
1. Init npm repo and install docsify-cli
    ```javascript
    npm install
    ```

1. Serve documentation locally
    ```javascript
    npm run docs
    ```


## Quick Start Template (Full featured)
Insert and replace following HTML into index.html:
> :fire: Don't forget to follow [Start documentation](#start-documentation) after copying this code snippet
> 
> Also create a _sidebar.md file according [Add a sidebar](#add-a-sidebar)

> :information_source: For more details on plugins used by this template please see [Plugins & configurations](docsify-docs/useful-plugins.md)

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>YOUR_AMAZING_TITLE</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
        <meta name="description" content="YOUR_INCREDIBLE_DESCRIPTION">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        <!-- Darklight theme customization-->
            <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify-darklight-theme@3/dist/docsify-themeable/style.min.css" type="text/css">
            <!-- docsify-themeable styles-->
            <link rel="stylesheet alternative" href="https://cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-simple.css" title="light">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-simple-dark.css" title="dark">
            <!-- Custom theme styles -->
            <style>
                :root {
                    --content-max-width: 75em;
                    --sidebar-width: 25rem;
                }
            </style>
        <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.css">
        <script src="//cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    </head>

    <body>
        <div id="app"></div>
        <script>
            window.$docsify = {
                search: 'auto',
                name: 'LEAVE_IT_EMPTY_OR_ENTER_A_HOME_BUTTON_LABEL',
                repo: 'https://github.com/docsifyjs/docsify/',
                loadSidebar: true,
                subMaxLevel: 2,
                markdown: {
                    renderer: {
                        code: function (code, lang) {
                            if (lang === "mermaid") {
                                return (
                                    '<div class="mermaid">' + mermaid.render('mermaid-svg-' + num++, code) +
                                    "</div>"
                                );
                            }
                            return this.origin.code.apply(this, arguments);
                        }
                    }
                },
            }

            let num = 0;
            mermaid.initialize({
                startOnLoad: false
            });
        </script>
        <!-- Docsify v4 -->
        <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
        <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
        <script src="//cdn.jsdelivr.net/npm/docsify-copy-code"></script>
        
        <!-- Darklight theme customization-->
        <script src="//cdn.jsdelivr.net/npm/docsify-darklight-theme@3/dist/docsify-themeable/main.min.js"></script>
        <script src="//cdn.jsdelivr.net/npm/docsify-darklight-theme@3/dist/docsify-themeable/index.min.js"></script>
    </body>
</html>
```   


## Start documentation
1. Insert a title and description to the index.html newly created
    ```html
    <title>YOUR_AMAZING_TITLE</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="description" content="YOUR_INCREDIBLE_DESCRIPTION">
    ```

1. Add your git repo and if you want a home link in the top left corner add a name otherwise leave it empty to hide it
    ```html
    <script>
        window.$docsify = {
            name: 'LEAVE_IT_EMPTY_OR_ENTER_A_HOME_BUTTON_LABEL',
            repo: 'https://github.com/docsifyjs/docsify/'
        }
    </script>
    ```
   

## Add a sidebar
1. Add those lines in `window.$docsify` script
    ```html
    <script>
        window.$docsify = {
            //...
            loadSidebar: true,
            subMaxLevel: 2,
            //...           
        }
    </script>
    ```
   
1. Create a `_sidebar.md` in docs root folder and fill it like this
    ```markdown
    - Introduction
        - [About project](../README.md)
        - [Documenting with Docsify](start-documenting.md)
    ```

