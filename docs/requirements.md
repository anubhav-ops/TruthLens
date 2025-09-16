TruthLens requirements:-
1. Input System
	User can paste text, URL, or upload a document to fact-check.
2. AI-Powered Claim Extraction
	NLP model that identifies claims (statements that can be true/false) from text.
	Highlight those claims for the user.
3.	Evidence Retrieval
	Search trusted sources (news APIs, Wikipedia, research papers) to find relevant information.
	Rank results based on credibility & recency.
4.Fact-Checking Model
	ML/AI model classifies each claim as True, False, Misleading, or Unverified.
	Explainability: show WHY it was classified (source links, confidence score).
5.Result Presentation
	Clean, simple UI that shows:
		✅ True
		❌ False
		⚠️ Misleading
		❓ Needs more data
	Confidence score (e.g., 85% sure this is true).