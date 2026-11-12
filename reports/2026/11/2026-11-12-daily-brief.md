# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-11-12

> 📅 **Tarih:** 2026-11-12 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
- **Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects**: Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects: Gelişme detayları inceleniyor.
- **Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens**: Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens: Gelişme detayları inceleniyor.
- **[ArXiv] Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training**: [ArXiv] Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training: Gelişme detayları inceleniyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training](http://arxiv.org/abs/2611.14519v1)
**Öne Çıkanlar:**
  - [ArXiv] Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be adapted, and what determines this. We adapted a foundation model, DINOv2, with strategies ranging from tuning only its bias terms to full fine-tuning, and compared it with U-Nets and ResU-Nets trained from scratch. Experiments covered colonoscopy, breast ultrasound and dermoscopy, with testing on held-out data from the training source and on independent datasets from other institutions. The adapted foundation model generalised better on every external dataset. Within the training distribution, the task-specific models remained competitive when training data were abundant, and delineated boundaries more precisely, while the foundation model more often missed small lesions. Only a small fraction of the foundation model required adaptation, and the capacity needed was determined by the imaging domain rather than by the adaptation method. A widely used polyp test set was also found to duplicate images from another benchmark. Foundation-model adaptation is therefore warranted where models must work across sites, 

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2611.14519v1](http://arxiv.org/abs/2611.14519v1)

---

### [[ArXiv] Toward Foundation Detection Models via Example-Based Grounding in EM-DETR](http://arxiv.org/abs/2611.14518v1)
**Öne Çıkanlar:**
  - [ArXiv] Toward Foundation Detection Models via Example-Based Grounding in EM-DETR: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by integrating diverse medical image datasets annotated for both anatomical structures and abnormalities. We first propose a student-teacher training strategy to effectively combine datasets with heterogeneous label spaces, mitigating catastrophic forgetting, and im proving feature learning. In addition, building on our previously pro posed example-based EM-DETR framework, we adapt it to jointly learn from multiple domain-specific datasets, enabling fine-grained, example driven detection across modalities. Our model achieves state-of-the-art (SOTA) results, with image-level AUC scores exceeding previous SOTA by 1% point on four key findings in CXRs. We achieve a leading mAP50 in CXRs and mammography, surpassing EM-DETR trained on a single dataset by 2-3% points. This approach paves the way for scalable foundation models in medical imaging that leverage heterogeneous data while maintaining robust and generalizable performance.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2611.14518v1](http://arxiv.org/abs/2611.14518v1)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects](https://www.marktechpost.com/2026/11/11/google-deepmind-alphagenome-2-cell-type-variant-effects/)
**Öne Çıkanlar:**
  - Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Google DeepMind released AlphaGenome 2, a conditional DNA sequence model that predicts regulatory activity and variant effects per cell type. It is available via the AlphaGenome API for non-commercial research. The post Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/11/google-deepmind-alphagenome-2-cell-type-variant-effects/](https://www.marktechpost.com/2026/11/11/google-deepmind-alphagenome-2-cell-type-variant-effects/)

---

### [Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens](https://www.marktechpost.com/2026/11/11/google-gemini-decisions-api-gemini-decision-1/)
**Öne Çıkanlar:**
  - Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Google launched the Gemini Decisions API, powered by Gemini Decision 1. It returns calibrated probabilities for up to 1,000 yes/no, choice and rubric questions over text, images, audio, video and PDFs, at $0.10 per 1M input tokens. The post Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/11/google-gemini-decisions-api-gemini-decision-1/](https://www.marktechpost.com/2026/11/11/google-gemini-decisions-api-gemini-decision-1/)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | Google DeepMind Releases AlphaGenome 2 for Cell-Type-Specific Variant Effects | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/11/google-deepmind-alphagenome-2-cell-type-variant-effects/) |
| 2 | Google Launches Gemini Decisions API With Gemini Decision 1 at $0.10/M Tokens | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/11/google-gemini-decisions-api-gemini-decision-1/) |
| 3 | [ArXiv] Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training | `arxiv.org` | [İncele](http://arxiv.org/abs/2611.14519v1) |
| 4 | [ArXiv] Toward Foundation Detection Models via Example-Based Grounding in EM-DETR | `arxiv.org` | [İncele](http://arxiv.org/abs/2611.14518v1) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
