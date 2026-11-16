> **Level 2: Intermediate** · Topic 17 of 35

[← CSV Processing](./16-csv-processing.md) · [↑ Level index](../README.md) · [Logging →](./18-logging.md)

# XML Processing

## Overview
- **What is it?** XML processing parses, queries, and creates hierarchical XML documents used by many enterprise systems.
- **Why is it important?** Legacy integrations, document standards, and some APIs still require correct XML handling.
- **Where is it used?** SOAP services, RSS/Atom feeds, office document formats, and B2B data exchanges.

## Learning Objectives
- Navigate ElementTree elements and attributes.
- Handle XML namespaces.
- Parse untrusted or large XML with appropriate safeguards.

## Real World Applications
- Consume supplier catalogs delivered as XML.
- Generate compliant invoices for partner systems.
- Transform nested configuration documents safely.

## Core Concepts

### Element tree
- **Definition:** An XML document forms a tree of elements with tags, attributes, text, and child elements.
- **Visual explanation:** ``document root -> nested element nodes``
- **Practical example:**

```python
import xml.etree.ElementTree as ET
root = ET.fromstring("<catalog><book id='1'/></catalog>")
print(root.find("book").get("id"))
```

### Namespaces
- **Definition:** A namespace URI qualifies tag names; ElementTree queries use expanded names or a prefix mapping.
- **Visual explanation:** ``prefix:name -> {namespace URI}name``
- **Practical example:**

```python
import xml.etree.ElementTree as ET
root = ET.fromstring("<x:item xmlns:x='urn:shop'>Book</x:item>")
print(root.tag)
```

### Safety and streaming
- **Definition:** iterparse limits retained tree state for large files; untrusted XML may require defusedxml to block entity-based attacks.
- **Visual explanation:** ``large/untrusted XML -> safe parser -> incremental events``
- **Practical example:**

```python
import xml.etree.ElementTree as ET
for event, element in ET.iterparse("catalog.xml", events=("end",)):
    if element.tag == "book":
        element.clear()
```

## Infographic Summary

| Infographic Block | Topic-specific guidance |
| --- | --- |
| 📌 Concept | XML processing parses, queries, and creates hierarchical XML documents used by many enterprise systems. |
| ⚡ Purpose | ElementTree handles namespaces and escaped text while allowing incremental parsing for larger documents. |
| 🔥 Benefits | Namespace-aware document handling, safe hierarchical extraction, and scalable incremental parsing. |
| 🎯 Use Cases | enterprise integrations, feeds and configuration, document metadata |
| 🚀 Best Practices | Use namespace maps and a hardened parser when XML is untrusted. |
| ❌ Common Mistakes | Using regex to parse nested XML markup. |

## Syntax Guide

### Basic Syntax

```python
import xml.etree.ElementTree as ET

root = ET.fromstring("<user><name>Ada</name></user>")
print(root.findtext("name"))
```

### Standard Structure

```python
import xml.etree.ElementTree as ET

NS = {"atom": "http://www.w3.org/2005/Atom"}
root = ET.fromstring(xml_text)
titles = [node.text for node in root.findall("atom:entry/atom:title", NS)]
```

### Code Pattern

```python
# Parse with a trusted or hardened parser.
# Locate elements with namespace-aware paths.
# Validate required attributes and text.
# Clear processed nodes during incremental parsing.
```

## Examples

### Beginner Example

```python
import xml.etree.ElementTree as ET

xml_text = "<catalog><book id='7'><title>Python</title></book></catalog>"
root = ET.fromstring(xml_text)
book = root.find("book")
print(book.get("id"), book.findtext("title"))
```

### Intermediate Example

```python
import xml.etree.ElementTree as ET

feed = '''<feed xmlns="urn:news">
  <entry><title>Release</title></entry>
  <entry><title>Guide</title></entry>
</feed>'''
root = ET.fromstring(feed)
namespaces = {"news": "urn:news"}
titles = [node.text for node in root.findall("news:entry/news:title", namespaces)]
print(titles)
```

### Advanced Example

```python
import xml.etree.ElementTree as ET
from io import BytesIO

def iter_products(source):
    for event, element in ET.iterparse(source, events=("end",)):
        if element.tag == "product":
            sku = element.get("sku")
            price_text = element.findtext("price")
            if not sku or price_text is None:
                raise ValueError("product requires sku and price")
            yield {"sku": sku, "price": float(price_text)}
            element.clear()

document = b"<products><product sku='A1'><price>9.50</price></product></products>"
print(list(iter_products(BytesIO(document))))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Choose safe parser] --> B[Parse root or events]
    B --> C[Resolve namespaces]
    C --> D[Extract and validate nodes]
    D --> E[Clear or serialize elements]
```

---

[← CSV Processing](./16-csv-processing.md) · [↑ Level index](../README.md) · [Logging →](./18-logging.md)
