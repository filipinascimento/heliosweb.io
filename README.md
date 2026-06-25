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

The release build installs `helios-network@0.10.0` and `helios-web@0.10.0`.
During local release preparation the build script can also stage bundles from
adjacent `helios-network-v2/dist` and `helios-web-next/dist` directories.

## Versioned Docs

Docs versions follow Helios package releases. Tag this repository with
`v0.10.0` for the 0.10.0 release and deploy versioned docs with:

```sh
mike deploy --push --update-aliases 0.10.0 latest
```
