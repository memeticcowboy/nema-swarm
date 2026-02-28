# Deconstructing the Illusion of OpenAI's o1 Model: A Critical Analysis

Created at 2024/09/16 9:34 AM

Smoke and mirrors is all you need... Deconstructing Sam's o1 'magik' bs

Some are suggesting that the recent o1 model is based on the Q* process described in a paper published by OpenAI some time ago. However, after spending the weekend experimenting with the model, I do not believe that to be the case.

Unlike many others, I don’t think any reinforcement learning or reward algorithm is at play. What we’re seeing appears to be a generic Chain-of-Thought (CoT) process that breaks tasks into several steps, starting with headings like "Thinking" and "Analyzing." Subsequent steps seem to be generated based on context, but fundamentally, the model seems like a fine-tuned version of GPT-4. It likely outputs a structured JSON with the steps for each task, following the general CoT framework, which begins with "Thinking/Analyzing," adds task-specific headings, and ends with verification and summarization steps.

These steps are tracked continuously, with subsequent interactions being concatenated into the context, which is fed back into the model along with an updated CoT "script." On the interface, you see this CoT JSON rendered with cues like "Thinking" and "Analyzing," alongside other keywords designed to give the impression of deeper processing.

But in reality, this is essentially the same GPT-4 model, fine-tuned for specific issues but with very little else changed. The CoT module simply controls the flow of interaction, giving the illusion of more sophisticated intelligence.
Via [Denis O/LinkedIn](https://www.linkedin.com/posts/denis-o-b61a379a_smoke-and-mirrors-is-all-you-need-deconstructing-activity-7240951665556672512-HO-R?utm_source=share&utm_medium=member_desktop)


It’s mostly a gimmick—smoke and mirrors from OpenAI. The same issues remain. Sure, In-Context Learning (ICL) and CoT can lead to some improvements, but they will be marginal at best. 

There’s no actual thinking or reasoning happening. It’s still contextual inference, now wrapped in a CoT controller that follows a mostly scripted process with dynamic headings. This even adds some extra latency with each execution.

