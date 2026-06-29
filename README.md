# heliosweb.io

Standalone source for the Helios website and documentation.

- Homepage: https://heliosweb.io/
- App: https://heliosweb.io/app/
- Docs: https://heliosweb.io/docs/

## Build

```sh
python3 -m pip install -r requirements.txt
npm install
python3 scripts/build_docs.py
```

The release build installs `helios-network@0.10.3` and `helios-web@^0.10.9`.
The current website runtime, examples, and `/app/` route are staged from the
installed `helios-network` and `helios-web` npm packages. API reference
generation reads Helios Web and Helios Network source checkouts so generated
reference pages come from the repositories, not from generated bundles.

For local website work against checkout builds, use npm links by package name:

```sh
cd <helios-network checkout>
npm run build
npm link

cd <helios-web checkout>
npm run build
npm link

cd <heliosweb.io checkout>
npm run link:local
npm run build
```

`package.json` still keeps real npm package references for release builds; the
local link only changes what `node_modules` resolves to on this machine.

For a local source override, set `HELIOS_WEB_SOURCE` or
`HELIOS_NETWORK_SOURCE`. If a checkout is not present, Helios Web can fall back
to `node_modules/helios-web/src`; Helios Network still needs the source checkout
for Python and native C reference pages.

## Versioned Docs

Docs versions follow Helios package releases. Tag this repository with
`v0.10.9` for the 0.10.9 release and deploy versioned docs with:

```sh
mike deploy --push --update-aliases 0.10.9 latest
```
