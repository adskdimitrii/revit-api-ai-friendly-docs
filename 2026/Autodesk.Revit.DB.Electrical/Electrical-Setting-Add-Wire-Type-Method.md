# Electrical Setting Add Wire Type Method

Source: https://www.revitapidocs.com/2026/96fef9f1-166b-082d-1ec7-e844ac51297f.htm

---

| Electrical Setting Add Wire Type Method |
| --- |

**Note: This API is now obsolete.** 

Add a new wire type to project. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("
                  AddWireType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use WireType.Duplicate() instead.
                  WireMaterialType object can no longer set to the WireType, use property WireType.WireMaterial instead.
                  TemperatureRatingType object can no longer set to the WireType, use property WireType.TemperatureRating instead.
                  InsulationType object can no longer set to the WireType, use property WireType.Insulation instead.
                  MaxSize object can no longer set to the WireType, use property WireType.MaxSize instead.
               ")]
public WireType AddWireType(
	string name,
	WireMaterialType materialType,
	TemperatureRatingType temperatureRating,
	InsulationType insulation,
	WireSize maxSize,
	double neutralMultiplier,
	bool neutralRequired,
	NeutralMode neutralMode,
	WireConduitType conduit
)
```

```
<ObsoleteAttribute("
                  AddWireType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use WireType.Duplicate() instead.
                  WireMaterialType object can no longer set to the WireType, use property WireType.WireMaterial instead.
                  TemperatureRatingType object can no longer set to the WireType, use property WireType.TemperatureRating instead.
                  InsulationType object can no longer set to the WireType, use property WireType.Insulation instead.
                  MaxSize object can no longer set to the WireType, use property WireType.MaxSize instead.
               ")>
Public Function AddWireType ( 
	name As String,
	materialType As WireMaterialType,
	temperatureRating As TemperatureRatingType,
	insulation As InsulationType,
	maxSize As WireSize,
	neutralMultiplier As Double,
	neutralRequired As Boolean,
	neutralMode As NeutralMode,
	conduit As WireConduitType
) As WireType
```

```
public:
[ObsoleteAttribute(L"
                  AddWireType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use WireType.Duplicate() instead.
                  WireMaterialType object can no longer set to the WireType, use property WireType.WireMaterial instead.
                  TemperatureRatingType object can no longer set to the WireType, use property WireType.TemperatureRating instead.
                  InsulationType object can no longer set to the WireType, use property WireType.Insulation instead.
                  MaxSize object can no longer set to the WireType, use property WireType.MaxSize instead.
               ")]
WireType^ AddWireType(
	String^ name, 
	WireMaterialType^ materialType, 
	TemperatureRatingType^ temperatureRating, 
	InsulationType^ insulation, 
	WireSize^ maxSize, 
	double neutralMultiplier, 
	bool neutralRequired, 
	NeutralMode neutralMode, 
	WireConduitType^ conduit
)
```

```
[<ObsoleteAttribute("
                  AddWireType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use WireType.Duplicate() instead.
                  WireMaterialType object can no longer set to the WireType, use property WireType.WireMaterial instead.
                  TemperatureRatingType object can no longer set to the WireType, use property WireType.TemperatureRating instead.
                  InsulationType object can no longer set to the WireType, use property WireType.Insulation instead.
                  MaxSize object can no longer set to the WireType, use property WireType.MaxSize instead.
               ")>]
member AddWireType : 
        name : string * 
        materialType : WireMaterialType * 
        temperatureRating : TemperatureRatingType * 
        insulation : InsulationType * 
        maxSize : WireSize * 
        neutralMultiplier : float * 
        neutralRequired : bool * 
        neutralMode : NeutralMode * 
        conduit : WireConduitType -> WireType 
```

#### Parameters

name String
:   Name of the new wire type.

materialType [WireMaterialType](Wire-Material-Type-Class.md)
:   Wire material of new wire type.

temperatureRating [TemperatureRatingType](Temperature-Rating-Type-Class.md)
:   Temperature rating type information of new wire type.

insulation [InsulationType](Insulation-Type-Class.md)
:   Insulation of new wire type.

maxSize [WireSize](Wire-Size-Class.md)
:   Max wire size of new wire type.

neutralMultiplier Double
:   Neutral multiplier of new wire type.

neutralRequired Boolean
:   Specify whether neutral point is required.

neutralMode [NeutralMode](e8890ec2-1c61-1ff3-e4f6-8ad3ce9a431c.htm)
:   Specify neutral mode.

conduit [WireConduitType](3c17c9e5-7018-1cf6-4a20-d8059cec370c.htm)
:   Conduit type of new wire type.

#### Return Value

[WireType](Wire-Type-Class.md) 
New added wire type object. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Parameter of temperatureRating should be retrieved from parameter of materialType, 
and parameters such as insulation and maxSize should be retrieved from temperatureRating.
otherwise, this add operation is most likely to fail. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSetting Class](Electrical-Setting-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
