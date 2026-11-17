# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-11-17

> 📅 **Tarih:** 2026-11-17 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
- **[ArXiv] Latent Lattice Language Models**: [ArXiv] Latent Lattice Language Models: Gelişme detayları inceleniyor.
- **[ArXiv] ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization**: [ArXiv] ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization: Gelişme detayları inceleniyor.
- **NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure**: NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure: Gelişme detayları inceleniyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] Latent Lattice Language Models](http://arxiv.org/abs/2611.21608v1)
**Öne Çıkanlar:**
  - [ArXiv] Latent Lattice Language Models: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Language models typically increase per-token computation through deeper or looped layers and latent reasoning steps, while richer residual connections improve information flow across layers. We instead increase computational capacity: the number of active computational states a model maintains. We introduce the Lattice of Latents, a set of per-layer horizontal latent streams that run recurrently along time, alongside the vertical residual stream that flows through depth. Like hyper-connections, mHC, and attention or value residuals, the Lattice enhances the residual stream, but rather than adding or rerouting residual pathways through depth, it provides companion computational states that persist across tokens. Unlike hybrid Transformer-SSM architectures, whose recurrent states primarily serve as internal memory for sequence mixing, these latents directly condition the vertical stream's attention, KV-cache writes, MLP computation, and decoding. On Transformers trained on 20B FineWeb-Edu tokens, a 406M-parameter Lattice model lowers validation perplexity from 15.41 to 14.40 over a parameter-matched Transformer. These gains extend across architectural variants. The Lattice composes with prior residual-stream enhancements: with hyper-connections and input residuals, it lowers validation perplexity from 15.41 (base Transformer) and 14.22 (Transformer with the same enhancements) to 13.61. On Gated DeltaNet, Mamba-2, Triadic GDN, and GDN-Mamba-2 hybrids, it improves perplexity at e

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2611.21608v1](http://arxiv.org/abs/2611.21608v1)

---

### [[ArXiv] ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization](http://arxiv.org/abs/2611.21605v1)
**Öne Çıkanlar:**
  - [ArXiv] ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Visual agents answer questions about ultra-high-resolution photos by zooming into the relevant regions. However, existing agents often answer from common sense instead of reading the evidence. Reinforcement learning (RL) on the final answer cannot correct this, because a guess earns the same reward as reading. We propose Cross-Input Relative Policy Optimization (CrossRPO), which trains agents on contrast sets. A contrast set asks one question about several versions of an image that differ only in a small region with the evidence and have different answers, so only reading the evidence solves the whole set. CrossRPO rewards solving the whole set, and we prove that it does not reinforce a set answered from common sense. We build contrast sets for training (ViRA-Train) and evaluation (ViRA-Bench) by editing one small object in images of 21 to 120 megapixels, and we photograph further sets with real changes (ViRA-Bench-Real) to exclude editing traces. We train two Visual Reasoning Agents, ViRA-9B and ViRA-27B, with CrossRPO on only about 3,500 items of ViRA-Train each. CrossRPO achieves 63.3% set accuracy on ViRA-Bench at the maximum resolution, against 59.3% for GRPO. ViRA-9B is the most accurate open model of its size on all benchmarks, and ViRA-27B outperforms Claude Haiku 5.5 and GPT-6-Luna, both at their highest thinking level, on most benchmarks.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2611.21605v1](http://arxiv.org/abs/2611.21605v1)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure](https://www.marktechpost.com/2026/11/17/nvidia-nvke-nvkr-managed-kubernetes-gpu/)
**Öne Çıkanlar:**
  - NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
NVIDIA has open-sourced NVIDIA Kubernetes Engine (NVKE) and NVIDIA Kubernetes Recipes (NVKR) under Apache 2.0. Together they let AI factories run a managed Kubernetes service on their own bare-metal GPU servers. Both are in public preview. The post NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Tooling alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/17/nvidia-nvke-nvkr-managed-kubernetes-gpu/](https://www.marktechpost.com/2026/11/17/nvidia-nvke-nvkr-managed-kubernetes-gpu/)

---

### [Liquid AI Releases d1.2 and d1.2-ultra: Omnimodal Decision Models That Top the AA Decision Index](https://www.marktechpost.com/2026/11/17/liquid-ai-d1-2-omnimodal-decision-models/)
**Öne Çıkanlar:**
  - Liquid AI Releases d1.2 and d1.2-ultra: Omnimodal Decision Models That Top the AA Decision Index: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Liquid AI released d1.2 and d1.2-ultra, decision models that read text, images and audio and return calibrated probabilities with zero output tokens. d1.2-ultra scores 75 on the Artificial Analysis Decision Index v2.1. The post Liquid AI Releases d1.2 and d1.2-ultra: Omnimodal Decision Models That Top the AA Decision Index appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/17/liquid-ai-d1-2-omnimodal-decision-models/](https://www.marktechpost.com/2026/11/17/liquid-ai-d1-2-omnimodal-decision-models/)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | [ArXiv] Latent Lattice Language Models | `arxiv.org` | [İncele](http://arxiv.org/abs/2611.21608v1) |
| 2 | [ArXiv] ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization | `arxiv.org` | [İncele](http://arxiv.org/abs/2611.21605v1) |
| 3 | NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/17/nvidia-nvke-nvkr-managed-kubernetes-gpu/) |
| 4 | Liquid AI Releases d1.2 and d1.2-ultra: Omnimodal Decision Models That Top the AA Decision Index | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/17/liquid-ai-d1-2-omnimodal-decision-models/) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
