
# Design Decisions at Version 0.1

> [!WARNING]
> **Alpha Software: Use at Your Own Risk.**
> Spore OS is currently in an alpha state.
> It is under active development, breaking changes are expected frequently.
> Do not use in production environments.

## A Few Notes

* My objective is to release earlier than comfortable in order to catch design and implementation issues earlier.
* I think open-source is important and want to support it while finding a road to monetization. I hope this project can support open-source and make others money too.
* Through documents I use first and third-person interchangeably. At release it's just me. The "we" is aspirational.

- The Spore OS protocol and implementation are designed for flexibility and human readability over strict typing and performance.
- Early iterations will have "concepts of ideas" of a security model, but at these early stages the system assumes a local, trusted environment.
- Input and output validation is manual. This is intentional so that nodes can define and call one another with relative ease.
- Everything sent through the hub is logged. Do not send secrets, passwords, etc.
