# Electrical Setting Add Wire Material Type Method

Source: https://www.revitapidocs.com/2026/bda3127d-4237-2400-aae0-2e3d9d861a98.htm

---

| Electrical Setting Add Wire Material Type Method |
| --- |

**Note: This API is now obsolete.** 

Add a new type of wire material. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("AddWireMaterialType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorMaterial.Create() instead.")]
public WireMaterialType AddWireMaterialType(
	string name,
	WireMaterialType baseMaterial
)
```

```
<ObsoleteAttribute("AddWireMaterialType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorMaterial.Create() instead.")>
Public Function AddWireMaterialType ( 
	name As String,
	baseMaterial As WireMaterialType
) As WireMaterialType
```

```
public:
[ObsoleteAttribute(L"AddWireMaterialType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorMaterial.Create() instead.")]
WireMaterialType^ AddWireMaterialType(
	String^ name, 
	WireMaterialType^ baseMaterial
)
```

```
[<ObsoleteAttribute("AddWireMaterialType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorMaterial.Create() instead.")>]
member AddWireMaterialType : 
        name : string * 
        baseMaterial : WireMaterialType -> WireMaterialType 
```

#### Parameters

name String
:   Name of new material type.

baseMaterial [WireMaterialType](Wire-Material-Type-Class.md)
:   Specify an existing material type which New material will be constructed based on.

#### Return Value

[WireMaterialType](Wire-Material-Type-Class.md) 
New added wire material type object. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSetting Class](Electrical-Setting-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
