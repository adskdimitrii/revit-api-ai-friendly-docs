# Shape Importer Source Format Enumeration

Source: https://www.revitapidocs.com/2026/556c092a-0afa-c38e-c784-3d9d919dc220.htm

---

| Shape Importer Source Format Enumeration |
| --- |

An enumerated type listing the possible formats supported by ShapeImporter. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum ShapeImporterSourceFormat
```

```
Public Enumeration ShapeImporterSourceFormat
```

```
public enum class ShapeImporterSourceFormat
```

```
type ShapeImporterSourceFormat
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| Auto | 0 | The format of the incoming data will be determined from input file extension. |
| OBJ | 4 | The incoming data is in OBJ format (\*.obj). |
| Rhino | 2 | The incoming data is in Rhino format (\*.3dm). |
| SAT | 1 | The incoming data is in SAT format (\*.sat). |
| SketchUp | 3 | The incoming data is in SketchUp format (\*.skp). |
| STEP | 11 | The incoming data is in STEP format (\*.step, \*.stp, \*.stpz). |
| STL | 5 | The incoming data is in STL format (\*.stl). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
