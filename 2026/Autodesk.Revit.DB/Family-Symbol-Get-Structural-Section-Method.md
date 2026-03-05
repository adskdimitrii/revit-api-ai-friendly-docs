# Family Symbol Get Structural Section Method

Source: https://www.revitapidocs.com/2026/99fb2804-0763-d6d1-13e7-7f49ff85fb68.htm

---

| Family Symbol Get Structural Section Method |
| --- |

Gets the structural section from element. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public StructuralSection GetStructuralSection()
```

```
Public Function GetStructuralSection As StructuralSection
```

```
public:
StructuralSection^ GetStructuralSection()
```

```
member GetStructuralSection : unit -> StructuralSection 
```

#### Return Value

[StructuralSection](65b59d7d-bd7b-c71b-7159-dfc506a912ee.htm) 
The structural section. if the family symbol does not contain a structural section. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Only beams, braces and structural columns can have a structural section.
 To check if the element can have structural section use the [CanHaveStructuralSection](d78f43f9-9744-2f76-41d3-ff7506e7a35a.htm) method. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
