# Elova engagement (TEST, separate from the posting engine)
Branch `engage`. Does not touch main/engine/assets or Make.com.
Test: add secrets IG_SESSIONID (+IG_CSRF, IG_DS_USER_ID) from a TEST Instagram account, plus CF_ACCOUNT_ID and CF_API_TOKEN, run workflow engage-test with dry_run=1, then 0.
A workflow only appears in Actions once its file is on the default branch; use a separate repo for this, or copy engage.yml to main (it changes nothing else).
