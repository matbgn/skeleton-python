# General OOP Guidelines

---

> :information_source: Based on [Learn Python 3 the Hard Way](https://www.amazon.com/Learn-Python-Hard-Way-Introduction/dp/0134692888) from Zed Shaw (Author)



1. Write/Draw about the problem:
    1. Notes + Drawings + Descriptions
    1. In english paragraphs
    1. Or extensive Drawings
    
1. Describe each situation with [Job Stories](https://uxdesign.cc/better-stories-with-job-story-3467de354f45) alike (nouns + verbs)

1. Extract key concepts from Job Stories
    1. list nouns
    1. list verbs

    > :fire: Document yourself with analog situations, programs, technics, etc.

1. Create a Class Hierarchy Tree
    1. Class all nouns by asking:
        1. What is similar to this?
        1. What is basically another word for?
    
       ```
        * Noun
        * Noun
            * Noun
            * Noun
        ```

1. Map all verbs in the tree
    1. What actions are needed based on verbs list?
    1. What do I need in addition to achieve that?
    
        ```
        * Noun
            - Verb
            - Verb
        * Noun
            - Verb
            * Noun
            * Noun
        ```

1. Copy-paste the tree in your IDE and make it run with empty statements attributes.

    ```python
    class Noun:
        def __init__(self):
            pass
    ```

    ```java
    public class Noun {
        public Noun() {
            ;
        }
    }
    ```

1. Make unit tests to match the descriptions

    > :warning: Don't avoid it!

1. Start coding
1. Repeat and Refine