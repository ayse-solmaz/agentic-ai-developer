# Day 14 — JSON Encoding and Decoding

**Status:** Done (2026-09-01)  
**Phase:** 11–15 — day 4

## Goal

`Marshal` / `Unmarshal`, struct tags, `Encoder`/`Decoder`, `omitempty` and pointer optional fields.

## Check (your run)

```
marshal: {"name":"ada","age":19,"title":"eng"}
parsed: can 21 nick empty? true
encode:{"name":"efe","age":30}
decode: ali 3
omitempty nick/title: {"name":"ada","age":19}
```

Unknown JSON key `extra` ignored.

## Next

Day 15 — phase practice.
