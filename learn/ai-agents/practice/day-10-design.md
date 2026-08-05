# Day 10 — Personal Agent: Yoyo

## Goal
Kullanıcının günlük görevlerini kaydeder, hatırlatır; yapılmayanları ertesi güne taşır.

## MVP scope (şimdi)
- Görevleri yerel dosyada sakla (JSON) — gerçek Google Calendar / push sonra
- Komutlar: ekle, listele, yapıldı, ertele, sil, hatırlat
- Short-term: bugünün listesi (oturum)
- Long-term: haftalık görevler + dünden kalanlar (dosya)

## Tools (MVP)
- `add_task(title, day)`
- `list_tasks(day?)`
- `complete_task(id)`
- `snooze_task(id)` → yarına taşı
- `delete_task(id)`
- `remind_today()` → bugün + dünden taşınanlar


## Memory
- Short-term: bu sohbette hangi komutlar / bugünün görünümü
- Long-term: `tasks.json` (haftalık + snooze edilmiş görevler)

## Success criteria
1. Dün tamamlanmayan görev, bugün `hatırlat` / `listele` ile tekrar görünür
2. `ertele` sonrası görev yarın listesinde; `sil` sonrası listede yok

## Showcase (30 sn)
"Yoyo haftalık görevlerimi tutuyor. Demo: görev ekledim → listeledim → birini yapmadım diye erteledim → ertesi gün hatırlatınca o görev yine çıktı. Hafıza dosyada; bildirim/takvim bir sonraki sürüm."