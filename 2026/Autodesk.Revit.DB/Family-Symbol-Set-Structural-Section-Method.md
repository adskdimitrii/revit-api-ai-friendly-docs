# Family Symbol Set Structural Section Method

Source: https://www.revitapidocs.com/2026/c3348673-0c95-eaf6-9d89-8cd8c81b48f6.htm

---

| Family Symbol Set Structural Section Method |
| --- |

Sets the structural section in element. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetStructuralSection(
	StructuralSection structuralSection
)
```

```
Public Sub SetStructuralSection ( 
	structuralSection As StructuralSection
)
```

```
public:
void SetStructuralSection(
	StructuralSection^ structuralSection
)
```

```
member SetStructuralSection : 
        structuralSection : StructuralSection -> unit 
```

#### Parameters

structuralSection [StructuralSection](65b59d7d-bd7b-c71b-7159-dfc506a912ee.htm)
:   Structural section with values that will be set.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FamilySymbol cannot have a structural section. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Only beams, braces and structural columns can have a structural section.
 To check if the element can have structural section use the [CanHaveStructuralSection](d78f43f9-9744-2f76-41d3-ff7506e7a35a.htm) method. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
