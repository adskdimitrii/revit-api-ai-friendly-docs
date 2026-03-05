# Shape Importer Is Service Available Method

Source: https://www.revitapidocs.com/2026/74c90acb-a638-f840-afbe-d3cf5f78bf23.htm

---

| Shape Importer Is Service Available Method |
| --- |

Checks whether the data conversion service and Material Library are available. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool IsServiceAvailable()
```

```
Public Shared Function IsServiceAvailable As Boolean
```

```
public:
static bool IsServiceAvailable()
```

```
static member IsServiceAvailable : unit -> bool 
```

#### Return Value

Boolean 
True if the data conversion service and Material Library are available, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks ShapeImporter relies on optional data conversion functionality. This function checks whether it is available. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ShapeImporter Class](Shape-Importer-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
