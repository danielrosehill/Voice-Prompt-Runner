# Voice Prompt Runner - Demo Walkthrough

This page demonstrates a complete run through the Voice Prompt Runner pipeline, showing how spoken input transforms into structured AI output through three processing stages.

## 📁 Demo Files

- **Audio Input**: [`prompts/audio/demo.mp3`](prompts/audio/demo.mp3)
- **Stage 1 Output**: [`prompts/transcript/formatted/raw_demo_20251003_140333.txt`](prompts/transcript/formatted/raw_demo_20251003_140333.txt)
- **Stage 2 Output**: [`prompts/transcript/polished/optimized_demo_20251003_140333.md`](prompts/transcript/polished/optimized_demo_20251003_140333.md)
- **Stage 3 Output**: [`outputs/demo_20251003_140333_output.md`](outputs/demo_20251003_140333_output.md)

---

## Pipeline Stages

### 🎤 Stage 1: Audio Transcription

The pipeline begins by transcribing the audio file, removing filler words and adding natural sentence spacing.

**Excerpt from raw transcript:**

> I'd like to guess your recommendations for a headless CMS. Here's what I'm looking for and why I'm looking for something.
>
> A couple of years ago, I migrated from using WordPress sites to using static sites. A big part of my reason for doing so was wanting to not have to manage individual projects and backends and keep WordPress updated, which I always thought was kind of bloated. So I discovered static site generators...

**Key transformations:**
- Filler words removed (um, uh, like, you know)
- Natural paragraph breaks added
- Conversational tone preserved

📄 [View full transcript →](prompts/transcript/formatted/raw_demo_20251003_140333.txt)

---

### ✨ Stage 2: Prompt Optimization

The raw transcript is restructured into a well-organized, structured prompt suitable for AI processing. This stage also corrects transcription errors through contextual inference.

**Excerpt from optimized prompt:**

> ### **AI Prompt: Headless CMS Recommendation Request**
>
> **Objective:**
> Provide recommendations for a headless CMS that meets specific technical and budgetary requirements.
>
> **User Background & Journey:**
>
> *   **Initial Migration:** Migrated from WordPress to static sites a few years ago to reduce backend management overhead and perceived bloat.
> *   **Static Site Generator Experience:** Utilized static site generators but found content creation through code editors tied to a local environment cumbersome and inconvenient for remote work.
> *   **Current Setup:**
>     *   Uses Contentful as a headless CMS.
>     *   Front-end development with Astro.
>     *   Websites often feature technical projects, data sets, and Git repositories.
>
> **Core Requirements for a Headless CMS:**
>
> 1.  **Seamless Content Creation & Management:**
>     *   A user-friendly interface for content creators, moving beyond code-editor-based workflows.
>     *   Ability to create content from anywhere, not just a local environment.
>
> 2.  **Data Source Integrations:**
>     *   **High Priority:** Integrations with external data sources (e.g., Git repositories, data sets)...

**Key transformations:**
- Clear headers and hierarchical structure added
- Scattered ideas organized into logical sections (Background, Requirements, Concerns)
- Technical details properly formatted
- Core requirements extracted and prioritized
- Transcription errors corrected through context

📄 [View full optimized prompt →](prompts/transcript/polished/optimized_demo_20251003_140333.md)

---

### 🎯 Stage 3: LLM Execution

The optimized prompt is executed by an LLM to generate the final, actionable output.

**Excerpt from final output:**

> ## AI Response: Headless CMS Recommendations
>
> Based on your detailed requirements and journey, here are several headless CMS recommendations that aim to balance user-friendliness, data integration, affordability, and robust asset management...
>
> ### **Top Recommendations:**
>
> 1.  **Sanity.io**
>
>     *   **Why it fits:**
>         *   **Seamless Content Creation:** Sanity offers a highly customizable and intuitive "Sanity Studio" which is built in React...
>         *   **Scalability & Affordability:** Sanity has a generous free tier. Their paid tiers are structured more granularly than Contentful's, offering a "developer" plan that starts at $99/month...
>
> 2.  **Payload CMS**
>
>     *   **Why it fits:**
>         *   **Seamless Content Creation:** Payload is built with an admin UI that is highly intuitive and extensible...
>         *   **Scalability & Affordability:** Payload is **open-source and self-hostable**. This is its biggest advantage for cost...
>
> 3.  **Directus**
>
>     *   **Why it fits:**
>         *   **Schema Creation:** Directus features a visual UI for creating data models (tables and fields), which directly addresses your requirement...

**Key outputs:**
- Comprehensive recommendations tailored to requirements
- Detailed analysis of each option
- Pros/cons breakdown
- Implementation strategy
- Direct answers to original question

📄 [View full output →](outputs/demo_20251003_140333_output.md)

---

## Quality Progression

### Stage 1 → Stage 2 Improvements

The optimization stage transformed a rambling, conversational transcript into a structured, professional prompt:

| Aspect | Raw Transcript | Optimized Prompt |
|--------|---------------|------------------|
| **Structure** | Stream-of-consciousness | Hierarchical sections with headers |
| **Organization** | Ideas scattered throughout | Logically grouped by topic |
| **Clarity** | Conversational, repetitive | Concise, clear bullet points |
| **Formatting** | Plain text paragraphs | Markdown with proper hierarchy |
| **Errors** | "guess your recommendations" (likely "get") | Corrected through context |

### Stage 2 → Stage 3 Improvements

The execution stage generated actionable, detailed recommendations:

| Aspect | Optimized Prompt | Final Output |
|--------|-----------------|--------------|
| **Format** | Requirements document | Solutions with analysis |
| **Content** | Problem statement | Specific recommendations |
| **Detail** | High-level needs | Implementation details |
| **Actionability** | Describes what's needed | Provides concrete options |
| **Analysis** | User's constraints | Comparative evaluation |

---

## Error Correction Example

One notable correction demonstrates the contextual inference capability:

**Stage 1 (Transcription):**
> "I'd like to **guess** your recommendations for a headless CMS."

This appears to be a mishearing of "get" as "guess". The optimization stage doesn't explicitly fix this but restructures it more clearly:

**Stage 2 (Optimization):**
> "**Objective:** Provide recommendations for a headless CMS..."

The intent is preserved and clarified without the ambiguous "guess/get" phrasing.

---

## Key Takeaways

1. **Voice is more natural**: The speaker could elaborate on complex requirements naturally through speech
2. **Multi-stage refinement works**: Each stage progressively improved quality and structure
3. **Context fixes errors**: Transcription mishearings were corrected through contextual understanding
4. **Long-form prompts shine**: Complex requirements were captured that would be tedious to type
5. **Transparency aids iteration**: Access to all stages allows understanding and refinement

---

## Running the Demo

To reproduce this demo:

```bash
cd cli
python voice_prompt.py ../prompts/audio/demo.mp3
```

The pipeline will generate new timestamped files showing the same transformation process.
