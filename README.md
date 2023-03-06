# aura.ai

Are you looking for a way to transcribe and summarize online meetings and other voice-based activities without compromising your privacy or security? Do you want to have full control over your data and process it locally on your device? If so, you might be interested in aura.ai, an open-source software that allows you to do just that.

aura.ai is a powerful and easy-to-use tool that can automatically transcribe and summarize any audio input from online meetings, podcasts, lectures, interviews, and more. It uses state-of-the-art speech recognition and natural language processing algorithms to generate accurate and concise summaries of the main points and action items from your audio files. You can also edit, export, and share your transcripts and summaries with others.

Unlike other transcription and summarization services that require you to upload your data to the cloud, aura.ai runs entirely on your local device. This means that you don’t have to worry about data breaches, unauthorized access, or third-party interference. You can also customize the settings and parameters of aura.ai to suit your specific needs and preferences.

We hope that aura.ai will help you make the most out of your online meetings and voice-based activities. Try it today and see for yourself how aura.ai can transform your audio into actionable insights.

## Git workflow

This project will use the [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) for Git. All temporary branches (features, bugs, hotfixes, etc.) must be created and pushed to the "development" branch, the "development" branch will only get merged to main when a stable version is ready. Each release will be tagged as "vMajor.Minor.Patch" according to the [Semantic Versioning](https://semver.org/) definitions. Main will always contain the latest stable version.

### Branch names
Branch names should start with one of the following categories:
- bugfix: For branches working in an important bug fix.
- hotfix: For branches that introduces fast fixes to the codebase.
- feature: For branches that works on a new feature for the current version.
- experimental: When working with experimental stuff, commonly out of the scope of the version but that can be useful in the future.
- docs: For branches that introduces changes in documentation.

The naming convention should include the category, and a brief description of the branch work: _category_brief-branch-description_

for example:
- bugfix_solve-stop-recording-issue
- feature_implement-transcription-queue

### Commits 
Commits should be named as [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). 

