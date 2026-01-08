# CHANGELOG

## Unreleased

(Will be populated with future changes.)

## v0.5.0 - 2026-01-08

- Changed: All top-level imports normalized to `cvnets.*` to ensure package import resolution after installation.
- Moved: `data`, `utils`, `common`, `engine`, `metrics`, `loss_fn`, `optim`, `options` moved into `cvnets/` namespace.
- Changed: Relaxed dependency pins (converted `==` to `>=` in `constraints.txt` and `requirements.txt`). Note: **numpy must remain in the 1.x series** (e.g., `numpy>=1.21.2,<2.0`) to avoid ABI compatibility issues.
- Added: CI install-and-import smoke test to verify package importability after installation.
