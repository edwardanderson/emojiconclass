# Emojiconclass

Emojiconclass maps emojis to [Iconclass](http://iconclass.org/) concepts to help make indexing, accessing and understanding art more visual and fun.

The project aims to render complex ideas about artworks and the history of art into simple sequences of emojis which are intuitive to users regardless of knowledge, nationality or language.

Concepts are expressed by ordering and sequencing emojis. So for example [24: _the heavens (celestial bodies)_](http://iconclass.org/rkd/24/) may be written as 🌌, while [14: _astrology_](http://iconclass.org/rkd/14/) would be 🌌🤔. Longer sequences of emojis don't necessarily express ideas deeper in the Iconclass hierarchy: [26: _meteorological phenomena_](http://iconclass.org/rkd/26/) is ⛈️🤷 but [26E _thunderstorm_](http://iconclass.org/rkd/26E) is simply ⛈️.



## Version

This project is in very early development. Everything is likely to change.



## Linked Open Data

The Emojiconclass controlled vocabulary is implemented as Linked Open Data, and is available as JSON-LD.

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



## Examples

| Image                                                        | Emojiconclass                                | Iconclass code                                               |
| ------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| ![The Milkmaid, Johannes Vermeer, c. 1660](https://lh3.googleusercontent.com/cRtF3WdYfRQEraAcQz8dWDJOq3XsRX-h244rOw6zwkHtxy7NHjJOany7u4I2EG_uMAfNwBLHkFyLMENzpmfBTSYXIH_F=w300)<br />[The Milkmaid, Johannes Vermeer, c. 1660](http://hdl.handle.net/10934/RM0001.COLLECT.6417) | 👩‍🍳⛓️<br /> 🥛👩⛓️<br />🥛<br /> 🍞<br /> 🦶🔥<br />🏺 | [41C222](http://iconclass.org/41C222)<br />[47I22311](http://iconclass.org/47I22311)<br/>[41C6413](http://iconclass.org/41C6413)<br/>[41C621](http://iconclass.org/41C621)<br />[41B23](http://iconclass.org/41B23)<br/>[41A773](http://iconclass.org/41A773) |
| ![SK-C-5](https://lh3.googleusercontent.com/J-mxAE7CPu-DXIOx4QKBtb0GC4ud37da1QK7CzbTIDswmvZHXhLm4Tv2-1H3iBXJWAW_bHm7dMl3j5wv_XiWAg55VOM=w300)<br />[The Night Watch, Rembrandt van Rijn, 1642](http://hdl.handle.net/10934/RM0001.COLLECT.5216) | 💂🧑<br />⚔️👈<br />🥁👈<br />👧<br />💂🏴<br />🐕     | [45(+26)](http://iconclass.org/45(+26))<br />[45C1](http://iconclass.org/45C1)<br />[48C7341](http://iconclass.org/48C7341)<br />[31D11222](http://iconclass.org/31D11222)<br />[45D12](http://iconclass.org/45D12)<br />[34B11](http://iconclass.org/34B11) |
| ![SK-A-3262](https://lh3.googleusercontent.com/Ckjq-HkB2XhEsbuMsei0MR5fLTODfkcXY8qQTG-XLHVxE0jLO9DnSYaVE8n1kCrcm9AMKzoWB2w03LrY0v7eoj5hYw=w300)<br />[Self-portrait, Vincent van Gogh, 1887](http://hdl.handle.net/10934/RM0001.COLLECT.9617) | 🤳🖌️<br />👨‍🎨🤳<br />📜🙂                          | [48C513](http://iconclass.org/48C513)<br />[48B3](http://iconclass.org/48B3)<br />[61B2](http://iconclass.org/61B2) |



## Contributors

* Edward Anderson



## Licence

CC-BY