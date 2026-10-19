-- FR4: why each recommendation was made, written by the ML service only.
-- {"reason": "...", "probabilities": {"logistic_regression", "random_forest", "average"},
--  "top_factors": [{"feature", "label", "value", "direction"}], "matched_preference": null}
-- Students can still update only the status column (existing column grant).
alter table public.recommendations add column explanation jsonb;
