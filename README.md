# Emojiconclass

Emojiconclass maps emojis to [Iconclass](http://iconclass.org/) concepts to help make indexing, accessing and understanding art more visual and fun.

The project aims to render complex ideas about artworks and the history of art into simple sequences of emojis which are intuitive to users regardless of knowledge, nationality or language.



## 🖼️ Examples

| Image                                                        | Emojiconclass                                | Iconclass code                                               |
| ------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| ![The Milkmaid, Johannes Vermeer, c. 1660](https://lh3.googleusercontent.com/cRtF3WdYfRQEraAcQz8dWDJOq3XsRX-h244rOw6zwkHtxy7NHjJOany7u4I2EG_uMAfNwBLHkFyLMENzpmfBTSYXIH_F=w300)<br />[The Milkmaid, Johannes Vermeer, c. 1660](http://hdl.handle.net/10934/RM0001.COLLECT.6417) | 👩‍🍳⛓️<br /> 🥛👩⛓️<br />🥛<br /> 🍞<br /> 🦶🔥<br />🏺 | [41C222](http://iconclass.org/41C222)<br />[47I22311](http://iconclass.org/47I22311)<br/>[41C6413](http://iconclass.org/41C6413)<br/>[41C621](http://iconclass.org/41C621)<br />[41B23](http://iconclass.org/41B23)<br/>[41A773](http://iconclass.org/41A773) |
| ![SK-C-5](https://lh3.googleusercontent.com/J-mxAE7CPu-DXIOx4QKBtb0GC4ud37da1QK7CzbTIDswmvZHXhLm4Tv2-1H3iBXJWAW_bHm7dMl3j5wv_XiWAg55VOM=w300)<br />[The Night Watch, Rembrandt van Rijn, 1642](http://hdl.handle.net/10934/RM0001.COLLECT.5216) | 💂🧑<br />⚔️👈<br />🥁👈<br />👧<br />💂🏴<br />🐕     | [45(+26)](http://iconclass.org/45(+26))<br />[45C1](http://iconclass.org/45C1)<br />[48C7341](http://iconclass.org/48C7341)<br />[31D11222](http://iconclass.org/31D11222)<br />[45D12](http://iconclass.org/45D12)<br />[34B11](http://iconclass.org/34B11) |
| ![SK-A-3262](https://lh3.googleusercontent.com/Ckjq-HkB2XhEsbuMsei0MR5fLTODfkcXY8qQTG-XLHVxE0jLO9DnSYaVE8n1kCrcm9AMKzoWB2w03LrY0v7eoj5hYw=w300)<br />[Self-portrait, Vincent van Gogh, 1887](http://hdl.handle.net/10934/RM0001.COLLECT.9617) | 🤳🖌️<br />🤳<br />📜🙂                            | [48C513](http://iconclass.org/48C513)<br />[48B3](http://iconclass.org/48B3)<br />[61B2](http://iconclass.org/61B2) |



## 💡 Patterns

Emojis should be able to be used both literally and metaphorically. More elaborate ideas can be expressed by ordering and grouping sequences of different (or repeating) emojis. The following patterns show one way that the classes might be structured:



### 🏷️ names, ownership

* names of artefacts and man-made objects 🏺🏷️ [61G](http://iconclass.org/61G)
* names of historical events and situations 📜📅🏷️ [61I](http://iconclass.org/61I)
* mark of ownership ✍️🏷️ [49L27](http://iconclass.org/49L27)

### 🖼️ representations, allegories

* landscapes 🏞️🖼️ [25H](http://iconclass.org/25H)
* surrealia 🖼️⁉️ [29](http://iconclass.org/29)
* allegory of time and eternity 🖼️⏳ [23A](http://iconclass.org/23A)

### 🤔 abstraction, interpretation

* reasoning and the formation of ideas 💡🤔️ [52](http://iconclass.org/52)
* will, volition 👍🤔️ [53](http://iconclass.org/53)
* astrology 🌌🤔 [14](http://iconclass.org/14)

### 💭 knowledge, theory

* acoustics👂💭 [49E24](http://iconclass.org/49E24)
* thermodynamics ⚙️🔥💭 [49E23](http://iconclass.org/49E23)
* morality 💭🤔️ [57](http://iconclass.org/57)

### 👈 specificity, example

* handwriting, writing as activity ✍️👈 [49L11](http://iconclass.org/49L11)
* specific works of literature 📖👈 [83](http://iconclass.org/83)
* volcano 🌋👈 (not volcanism 🌋) [25C12](http://iconclass.org/25C12)



## 🔗 Linked Open Data

The Emojiconclass controlled vocabulary is implemented as Linked Open Data, and will be available as JSON-LD.

~~~json
{
  "@context": "content/ns/emojiconclass.json",
  "id": "http://www.emojiconclass.org/🎨🤔",
  "exact_match": {
    "id": "http://iconclass.org/0",
    "_label": "Abstract, Non-representational Art"
  }
}
~~~



## 🏗️ Version

This project is in very early development. Everything is likely to change.



## ✍️ Contributors

* [Edward Anderson](https://twitter.com/anderson_edw)



## ⚖️ Licence

CC-BY