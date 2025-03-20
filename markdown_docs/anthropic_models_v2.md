[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)

English

Search...

Ctrl K

Search...

Navigation

Models & pricing

All models overview

[Welcome](https://docs.anthropic.com/en/home) [User Guides](https://docs.anthropic.com/en/docs/welcome) [API Reference](https://docs.anthropic.com/en/api/getting-started) [Prompt Library](https://docs.anthropic.com/en/prompt-library/library) [Release Notes](https://docs.anthropic.com/en/release-notes/overview)

Introducing Claude 3.7 Sonnet- our most intelligent model yet. 3.7 Sonnet is the first hybrid [reasoning](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) model on the market. Learn more in our [blog post](http://www.anthropic.com/news/claude-3-7-sonnet).

[**Claude 3.5 Haiku** \\
\\
Our fastest model\\
\\
- Text and image input\\
- Text output\\
- 200k context window](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table)

[**Claude 3.7 Sonnet**](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table)

[Our most intelligent model](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table)

[Text and image input\\
Text output\\
200k context window](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table)- [Extended thinking](https://docs.anthropic.com/en/docs/about-claude/models/en/docs/build-with-claude/extended-thinking)

* * *

## [​](https://docs.anthropic.com/en/docs/about-claude/models/all-models\#model-names)  Model names

| Model | Anthropic API | AWS Bedrock | GCP Vertex AI |
| --- | --- | --- | --- |
| Claude 3.7 Sonnet | `claude-3-7-sonnet-20250219` ( `claude-3-7-sonnet-latest`) | `anthropic.claude-3-7-sonnet-20250219-v1:0` | `claude-3-7-sonnet@20250219` |
| Claude 3.5 Haiku | `claude-3-5-haiku-20241022` ( `claude-3-5-haiku-latest`) | `anthropic.claude-3-5-haiku-20241022-v1:0` | `claude-3-5-haiku@20241022` |

| Model | Anthropic API | AWS Bedrock | GCP Vertex AI |
| --- | --- | --- | --- |
| Claude 3.5 Sonnet v2 | `claude-3-5-sonnet-20241022` ( `claude-3-5-sonnet-latest`) | `anthropic.claude-3-5-sonnet-20241022-v2:0` | `claude-3-5-sonnet-v2@20241022` |
| Claude 3.5 Sonnet | `claude-3-5-sonnet-20240620` | `anthropic.claude-3-5-sonnet-20240620-v1:0` | `claude-3-5-sonnet-v1@20240620` |
| Claude 3 Opus | `claude-3-opus-20240229` ( `claude-3-opus-latest`) | `anthropic.claude-3-opus-20240229-v1:0` | `claude-3-opus@20240229` |
| Claude 3 Sonnet | `claude-3-sonnet-20240229` | `anthropic.claude-3-sonnet-20240229-v1:0` | `claude-3-sonnet@20240229` |
| Claude 3 Haiku | `claude-3-haiku-20240307` | `anthropic.claude-3-haiku-20240307-v1:0` | `claude-3-haiku@20240307` |

Models with the same snapshot date (e.g., 20240620) are identical across all platforms and do not change. The snapshot date in the model name ensures consistency and allows developers to rely on stable performance across different environments.

For convenience during development and testing, we offer “ `-latest`” aliases for our models (e.g., `claude-3-7-sonnet-latest`). These aliases automatically point to the most recent snapshot of a given model. While useful for experimentation, we recommend using specific model versions (e.g., `claude-3-7-sonnet-20250219`) in production applications to ensure consistent behavior. When we release new model snapshots, we’ll migrate the -latest alias to point to the new version (typically within a week of the new release). The -latest alias is subject to the same rate limits and pricing as the underlying model version it references.

### [​](https://docs.anthropic.com/en/docs/about-claude/models/all-models\#model-comparison-table)  Model comparison table

To help you choose the right model for your needs, we’ve compiled a table comparing the key features and capabilities of each model in the Claude family:

| Feature | Claude 3.7 Sonnet | Claude 3.5 Sonnet | Claude 3.5 Haiku | Claude 3 Opus | Claude 3 Haiku |
| --- | --- | --- | --- | --- | --- |
| **Description** | Our most intelligent model | Our previous most intelligent model | Our fastest model | Powerful model for complex tasks | Fastest and most compact model for near-instant responsiveness |
| **Strengths** | Highest level of intelligence and capability with toggleable extended thinking | High level of intelligence and capability | Intelligence at blazing speeds | Top-level intelligence, fluency, and understanding | Quick and accurate targeted performance |
| **Multilingual** | Yes | Yes | Yes | Yes | Yes |
| **Vision** | Yes | Yes | Yes | Yes | Yes |
| **[Extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)** | Yes | No | No | No | No |
| **API model name** | `claude-3-7-sonnet-20250219` | **Upgraded version:** `claude-3-5-sonnet-20241022`<br>**Previous version:** `claude-3-5-sonnet-20240620` | `claude-3-5-haiku-20241022` | `claude-3-opus-20240229` | `claude-3-haiku-20240307` |
| **Comparative latency** | Fast | Fast | Fastest | Moderately fast | Fastest |
| **Context window** | 200K | 200K | 200K | 200K | 200K |
| **Max output** | **Normal:** 8192 tokens<br>**[Extended thinking](https://docs.anthropic.com/en/docs/about-claude/models/en/docs/build-with-claude/extended-thinking):** 64000 tokens | 8192 tokens | 8192 tokens | 4096 tokens | 4096 tokens |
| **Cost (Input / Output per MTok)** | $3.00 / $15.00 | $3.00 / $15.00 | $0.80 / $4.00 | $15.00 / $75.00 | $0.25 / $1.25 |
| **Training data cut-off** | Nov 20241 | Apr 2024 | July 2024 | Aug 2023 | Aug 2023 |

_1 - While trained on publicly available information on the internet through November 2024, Claude 3.7 Sonnet’s knowledge cut-off date is the end of October 2024. This means the model’s knowledge base is most extensive and reliable on information and events up to October 2024._

Include the beta header `output-128k-2025-02-19` in your API request to increase the maximum output token length to 128k tokens for Claude 3.7 Sonnet.

We strongly suggest using our [streaming Messages API](https://docs.anthropic.com/en/api/messages-streaming) or [Batch API](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing) to avoid timeouts when generating longer outputs.
See our guidance on [long requests](https://docs.anthropic.com/en/api/errors#long-requests) for more details.

## [​](https://docs.anthropic.com/en/docs/about-claude/models/all-models\#prompt-and-output-performance)  Prompt and output performance

Claude 3.7 Sonnet excels in:

- **​Benchmark performance**: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the [Claude 3.7 blog post](http://www.anthropic.com/news/claude-3-7-sonnet) for more information.

- **Engaging responses**: Claude models are ideal for applications that require rich, human-like interactions.
  - If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to our [prompt engineering guides](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) for details.
- **Output quality**: When migrating from previous model generations to the Claude 3.7 Sonnet, you may notice larger improvements in overall performance.


* * *

## [​](https://docs.anthropic.com/en/docs/about-claude/models/all-models\#get-started-with-claude)  Get started with Claude

If you’re ready to start exploring what Claude can do for you, let’s dive in! Whether you’re a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, we’ve got you covered.

Looking to chat with Claude? Visit [claude.ai](http://www.claude.ai/)!

[**Intro to Claude** \\
\\
Explore Claude’s capabilities and development flow.](https://docs.anthropic.com/en/docs/intro-to-claude) [**Quickstart** \\
\\
Learn how to make your first API call in minutes.](https://docs.anthropic.com/en/docs/quickstart) [**Anthropic Console** \\
\\
Craft and test powerful prompts directly in your browser.](https://console.anthropic.com/)

If you have any questions or need assistance, don’t hesitate to reach out to our [support team](https://support.anthropic.com/) or consult the [Discord community](https://www.anthropic.com/discord).

Was this page helpful?

YesNo

[Legal summarization](https://docs.anthropic.com/en/docs/about-claude/use-case-guides/legal-summarization) [Extended thinking models](https://docs.anthropic.com/en/docs/about-claude/models/extended-thinking-models)

On this page

- [Model names](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-names)
- [Model comparison table](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table)
- [Prompt and output performance](https://docs.anthropic.com/en/docs/about-claude/models/all-models#prompt-and-output-performance)
- [Get started with Claude](https://docs.anthropic.com/en/docs/about-claude/models/all-models#get-started-with-claude)