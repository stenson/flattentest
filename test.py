from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
from fontPens.flattenPen import FlattenPen

glyph = TTFont("MutatorSans.ttf").getGlyphSet()["B"]

rp = RecordingPen()
fp = FlattenPen(rp, approximateSegmentLength=5)
glyph.draw(fp)