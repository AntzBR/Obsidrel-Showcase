# Contributor approval and release gate

> **DRAFT PROCESS.** No third-party asset can be published merely because a contributor sent the files or mentioned approval in chat.

1. **Identify the rights holder.** Confirm legal name or studio representative, contact channel, right to license, and any dependencies.
2. **Define the exact contribution.** Prepare an immutable file inventory with per-file relative path and SHA-256; attach it to Appendix A.
3. **Confirm public platform rights.** Inform contributors that GitHub's public repository terms permit platform viewing/forking and currently include AI/ML-related rights for GitHub and affiliates. Obtain explicit acceptance; otherwise **do not publish that asset to public GitHub**.
4. **Agree on use.** Ensure the contributor accepts public download, Minecraft resource-pack distribution to players, monetized servers, technical conversions, attribution, and continued permitted use of lawfully downloaded older versions.
5. **Execute private agreement.** Fill all placeholders, resolve the dispute clause, attach Appendix A and the referenced end-user license version; gather both electronic signatures. Store signed PDF, audit report and any private correspondence **outside the public repository**.
6. **Verify third-party licenses.** Do not use material from other publishers without adequate rights. Reject assets when incompatible conditions remain.
7. **Prepare public credits and release.** Add only approved attribution, the asset manifest, corresponding public license, and the approved content. Keep personal names, emails, contract PDFs, audit data and internal references private.
8. **Test before publishing.** Check contents, pack loading, YAML parsing, GUI visibility, SHA-256, and the exact generated Showcase ZIP on a staging server.

## Release blockers
- [ ] Contributor agreement executed and Appendix A approved
- [ ] All material rights and GitHub platform permissions confirmed
- [ ] Public end-user license finalized and consistent with contributor approval
- [ ] Official contact and attribution completed
- [ ] File manifest audited and assets approved
- [ ] Server, menu, pack, and release testing completed

## Documents
- [Draft end-user license](END-USER-CONTENT-LICENSE.DRAFT.md) — **not yet effective**
- `CONTENT-MANIFEST.template.csv` — empty inventory template; no rights are granted by listing a file
- Private contributor agreement — signed individually via Docusign and **never committed here**

The Obsidrel Core software license is independent of rights in any third-party Showcase assets.
