# 👁️ Argus-AI — Multi-Agent Intelligence System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/Orchestrator-LangGraph-orange.svg)](https://github.com/langchain-ai/langgraph)

> *Yunan mitolojisinde asla uyumayan ve her şeyi gören Argus'tan esinlenen; Deterministik LangGraph tabanlı, her gün otomatik olarak RSS kaynaklarını ve ArXiv makalelerini toplayan, puanlayan, derinlemesine analiz eden ve GitHub Actions ile arşivleyen otonom yapay zeka istihbarat gözcüsü.*

---

## 🏛️ Mimari ve Akış (System Architecture)

```
   [RSS Feeds / ArXiv API / HF Papers]
                       │
                       ▼
            ┌──────────────────────┐
            │ 1. Ingestion Worker  │ (Async paralel toplama & 24 saatlik tekilleştirme)
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   2. Curator Agent   │ (Relevance scoring: 1-10 & Pydantic filtreleme)
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   3. Analyst Agent   │ (Trafilatura ile tam metin kazıma & derin teknik analiz)
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │  4. Reporter Agent   │ (Yönetici özeti & Markdown bülten sentezi)
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   5. Auditor Agent   │ (Kalite Kapısı: Sızıntı kontrolü, link & format denetimi, auto-heal)
            └──────────┬───────────┘
                       ▼
  [Depolama: reports/YYYY/MM/YYYY-MM-DD-daily-brief.md + README/INDEX.md Güncellemesi]
                       │
                       ▼
            ┌──────────────────────┐
            │ 6. Broadcaster Agent │ (Telegram Kanalı/Sohbetine Anlık Mobil Bülten & GitHub Linki)
            └──────────┬───────────┘
                       ▼
         [GitHub Actions Otomatik Git Commit & Push]
                       │
                       ▼
         [Auditor Agent Post-Push Verification]
```

---

## 🚀 Özellikler

- **Çift LLM Desteği**: Hem Google Gemini hem de OpenAI ile tam uyumlu; `.env` üzerinden tek değişkenle geçiş (`LLM_PROVIDER=gemini` veya `openai`).
- **Kademeli Model Mimarisi**:
  - **Curator Agent**: Hızlı ve düşük maliyetli model (`gemini-3.8-flash` / `gpt-4o-mini`).
  - **Analyst Agent**: Derinlikli mimari, matematik ve benchmark analiz modeli (`gemini-3.8-flash` / `gpt-4o`).
- **Sıfır Halüsinasyon Link Güvencesi**: Raporlardaki bağlantılar asla uydurulmaz; doğrudan Ingestion katmanından gelen gerçek doğrulanmış URL'lerdir.
- **Fail-Safe Veri Toplama**: RSS veya arXiv kaynaklarından biri erişilemez olduğunda pipeline çökmez; hata loglanır ve kalan kaynaklarla devam edilir.
- **Dinamik Web Kazıma (Trafilatura)**: Önemli haberlerin sayfalarına bizzat gidilip tam metin/kod/benchmark bilgisi çekilir.
- **Auditor & Quality Assurance Agent**: Rapor oluşturulduktan sonra ve GitHub'a gönderildikten sonra devreye girer; ham LLM yanıtlarını, şifreleme imzalarını, Markdown sözdizimini ve link bütünlüğünü denetler, olası format bozukluklarını otomatik olarak onarır (auto-heal).
- **Broadcaster Agent (Telegram Yayını)**: Günlük rapor oluştuktan hemen sonra Yönetici Özeti (TL;DR) ve öne çıkan 5 haberi Telegram kanalınıza/grubunuza push bildirim olarak gönderir; GitHub'daki tam rapora doğrudan tıklanabilir bağlantı verir.
- **Dil Seçeneği**: Türkçe (`tr`) veya İngilizce (`en`) olarak tek ayarla rapor üretimi.
- **Otonom GitHub Actions**: Her sabah UTC 04:00 (TSİ 07:00) saatinde otomatik çalışır ve repo güncellenir.

---

## 📂 Dizin Yapısı

```
intelligence-agent/
├── .github/
│   └── workflows/
│       └── daily_brief.yml
├── config/
│   ├── sources.yaml
│   └── settings.py
├── src/
│   ├── __init__.py
│   ├── state.py
│   ├── ingest/
│   │   ├── __init__.py
│   │   ├── rss_collector.py
│   │   └── arxiv_collector.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── llm_factory.py
│   │   ├── curator.py
│   │   ├── analyst.py
│   │   └── reporter.py
│   ├── tools/
│   │   ├── __init__.py
│   │   └── web_scraper.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── archive_manager.py
│   └── graph.py
├── reports/
│   └── INDEX.md
├── tests/
├── .env.example
├── Dockerfile
├── requirements.txt
├── README.md
└── main.py
```

---

## ⚙️ Kurulum ve Yerel Çalıştırma

### 1. Depoyu Klonlayın ve Sanal Ortam Oluşturun
```bash
git clone https://github.com/hamzamalikyildiz/Argus-AI.git
cd Argus-AI

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Çevre Değişkenlerini Ayarlayın
`.env.example` dosyasını `.env` olarak kopyalayın ve API anahtarınızı girin:
```bash
cp .env.example .env
```
Örnek `.env` içeriği:
```ini
LLM_PROVIDER=gemini
GEMINI_API_KEY=AIzaSy...
CURATOR_MODEL=gemini-3.8-flash
ANALYST_MODEL=gemini-3.8-flash
REPORT_LANGUAGE=tr
```

### 3. Pipeline'ı Çalıştırın
```bash
python main.py
```
Özel parametrelerle çalıştırmak için:
```bash
# Belirli bir tarih ve dil ile çalıştırma
python main.py --date 2026-10-19 --lang tr
```

---

## 📰 Son Raporlar Arşivi

<!-- RECENT_REPORTS_START -->
| Tarih | Başlık / Odak Noktası | Rapor Linki |
|:---:|:---|:---:|
| 2026-10-31 | [ArXiv] Rethinking Neural Thickets Without Weight Perturbati | [Raporu Oku](reports/2026/10/2026-10-31-daily-brief.md) |
| 2026-10-30 | Mistral releases weights for its trillion-parameter AI model | [Raporu Oku](reports/2026/10/2026-10-30-daily-brief.md) |
| 2026-10-29 | NVIDIA Releases Nemotron 3.5 Transcribe, Google DeepMind Int | [Raporu Oku](reports/2026/10/2026-10-29-daily-brief.md) |
| 2026-10-28 | Polymathic AI and Princeton Researchers Release FlashMap, a  | [Raporu Oku](reports/2026/10/2026-10-28-daily-brief.md) |
| 2026-10-27 | OpenAI Launches GPT-6.1 Terra, Halving GPT-6.1 Sol’s API Pri | [Raporu Oku](reports/2026/10/2026-10-27-daily-brief.md) |
| 2026-10-26 | Hugging Face Releases Carbon-X, a 14B Open DNA Language Mode | [Raporu Oku](reports/2026/10/2026-10-26-daily-brief.md) |
| 2026-10-24 | Kyutai CADRE, Moonshot AI Releases Kimi K3.1 Pro | [Raporu Oku](reports/2026/10/2026-10-24-daily-brief.md) |
| 2026-10-23 | [ArXiv] Low-Bit N-Gram Embeddings for Language Models, [ArXi | [Raporu Oku](reports/2026/10/2026-10-23-daily-brief.md) |
| 2026-10-22 | Günlük AI Bülteni | [Raporu Oku](reports/2026/10/2026-10-22-daily-brief.md) |
| 2026-10-21 | Mistral AI Releases Voxtral 3, Google Cloud Ships llm-d 1.0  | [Raporu Oku](reports/2026/10/2026-10-21-daily-brief.md) |

[Tüm Arşivi Gör (reports/INDEX.md)](reports/INDEX.md)
<!-- RECENT_REPORTS_END -->

---

## 🤖 GitHub Actions ile Otomasyon ve Telegram Kurulumu

Sistem her sabah **UTC 04:00 (TSİ 07:00)** saatinde GitHub Actions üzerinde otonom çalışır; raporu derler, denetler, depoya arşivler ve Telegram kanalınıza bülten özeti gönderir.

### 1. GitHub Repository Secrets Ekleme
GitHub deponuzda **Settings > Secrets and variables > Actions** sayfasına gidin ve aşağıdaki `Repository secrets` tanımlarını yapın:

| Secret Adı | Zorunlu mu? | Açıklama |
|:---|:---:|:---|
| `GEMINI_API_KEY` | Evet* | Google Gemini API anahtarı (*OpenAI kullanıyorsanız `OPENAI_API_KEY`) |
| `TELEGRAM_BOT_TOKEN` | Opsiyonel | `@BotFather` üzerinden aldığınız bot token'ı |
| `TELEGRAM_CHAT_ID` | Opsiyonel | Mesajın gönderileceği kanal kullanıcı adı (örn: `@yapayzeka_bulteni`) veya Chat ID |
| `USER_EMAIL` | Opsiyonel | Commit geçmişinizde yeşil karelerin (contributions) size yazılması için GitHub e-postanız |
| `USER_NAME` | Opsiyonel | Commit atan kullanıcı adı (Varsayılan: `hamzamalikyildiz`) |

### 2. Telegram Kanalı Hazırlama (3 Adım)
1. Telegram'da **@BotFather** botuna gidip `/newbot` komutuyla bir bot oluşturun ve verilen `HTTP API Token`'ı `TELEGRAM_BOT_TOKEN` olarak GitHub Secrets'a ekleyin.
2. Telegram'da yeni bir **Kanal** veya **Grup** açın.
3. Botunuzu bu kanala/gruba **Yönetici (Admin)** olarak ekleyin ve "Mesaj Gönderme (Post Messages)" izni verin. Kanalınız genel ise `@kanal_adiniz`, gizli ise chat ID'sini `TELEGRAM_CHAT_ID` olarak ekleyin.

### 3. Workflow İzinleri
- GitHub deponuzda **Settings > Actions > General > Workflow permissions** sekmesine gidin.
- **"Read and write permissions"** seçeneğini seçip kaydedin (Actions'ın raporları repo'ya commit edebilmesi için gereklidir).

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına göz atabilirsiniz.
