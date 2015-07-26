from fir_artifacts.artifacts import AbstractArtifact


class Tag(AbstractArtifact):
	key = 'tag'
	display_name = 'Tags'
	regex = r"(?P<search>N0t a v@lid Regex)"
