import re
import sys

import enchant

from .language import RegexLanguage

badwords = [
    r"ה?קא?ק(י|ות|ה)",
    r"ה?חרא",
    r"חארות",
    r"[למ]חרבן",
    r"פיפי",
    r"(ב|ל|מ?ה)תחת",
    r"סקס",
    r"ה?זין",
    r"ציצים?",
    r"ה?בולבול(?:ים)?",
    r"זיו(ן|נים)",
    r"[מת]זד?יי(ן|נת|נים|נות|נו)",
    r"להזדיין",
    r"לזיין",
    r"למצוץ",
    r"מוצ(ץ|צת)",
    r"שפיך",
    r"ה?דפוק(ה|ים)?",
    r"ה?הומו",
    r"ה?גיי",
    r"קוקסינל",
    r"סקסי",
    r"יבני",
    r"ה?זונ(ה|ות)",
    r"בנזונה",
    r"שרמוט(ה|ות)",
    r"ה?מניאק",
    r"ה?מטומט(ם|מת|מי)",
    r"דביל(?:ים)?",
    r"טמבל",
    r"מפגר(?:ים)?",
    r"ה?מהממת",
    r"ה?כוס(ון|ית|יות)",
    r"אחושרמוטה",
    r"ה?פלו(ץ|צים)",
    r"[המ]פלי(ץ|צה)",
    r"להפליץ",
    r"מסריח(ים|ה)?",
    r"מגעיל",
    r"נוד",
    r"שטויות",
    r"היוש",
    r"חיימשלי",
    r"כאפות",
    r"כפרע",
    r"דגכ",
    r"זובי"
]
informals = [
    r"חחח+",
    r"[בה]ייי",
    r"פהה+",
    r"מכוערת?",
    r"מעפ(ן|נה)",
    r"ו?חתיך",
    r"אחלה",
    r"ה?חמוד(ה|ים)?",
    r"יאלל?ה",
    r"טעים",
    r"(בלה)+",
    r"סתם",
    r"כנסו",
    r"אות(כם|ך+)",
    r"שתדע",
    r"תהנו",
    r"לכו",
    r"לכם",
    r"בגללך",
    r"עליי",
    r"של(יי|כם|ך)",
    r"תיכנסו",
    r"אתם",
    r"אוהבת",
    r"מגניב",
    r"כיף",
    r"הדגדגנים",
    r"חזיות",
    r"[בל]פורנוגרפיה",
    r"משו?עמ(מים|ם)",
    r"אהה",
    r"יימח"
]
try:
    dictionary = enchant.Dict("he")
except enchant.errors.DictNotFoundError:
    raise ImportError("No enchant-compatible dictionary found for 'he'.  " +
                      "Consider installing 'myspell-he'.")



sys.modules[__name__] = RegexLanguage(
    __name__,
    badwords=badwords,
    informals=informals,
    dictionary=dictionary
)
"""
Implements :class:`~revscoring.languages.language.RegexLanguage` for Hebrew.
:data:`~revscoring.languages.language.is_badword`,
:data:`~revscoring.languages.language.is_misspelled`, and
:data:`~revscoring.languages.language.is_informal_word` are provided.
"""
